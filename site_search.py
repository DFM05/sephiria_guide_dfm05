"""全站搜索。

条目直接用 ast 从各页面源码里的数据常量（BUILD_CATEGORIES、PRESET_DATA 等）解析出来，
不执行页面脚本，所以页面新增内容后搜索索引会自动同步，不需要另外维护一份列表。

- 侧边栏搜索框和「全站搜索」页都把整份索引（含预先算好的拼音）交给浏览器，
  边输入边筛选，不和服务器通信、不刷新页面；
- 侧边栏 / 主页搜索框回车后跳到「全站搜索」页展示全部结果。

用到的开源项目：
- Fuse.js（https://github.com/krisk/Fuse，Apache-2.0，已放在 assets/vendor/fuse.js/）：浏览器端容忍错字的模糊匹配
- pypinyin（https://github.com/mozillazg/python-pinyin）：生成拼音 / 拼音首字母，支持拼音搜索
"""

from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urlencode

import streamlit as st
import streamlit.components.v1 as components
from pypinyin import Style, lazy_pinyin


ROOT_DIR = Path(__file__).resolve().parent
MAIN_SCRIPT = ROOT_DIR / "sephiriadfm05.py"
FUSE_JS = ROOT_DIR / "assets" / "vendor" / "fuse.js" / "fuse.basic.min.cjs"
SEARCH_PAGE = "search_page.py"


@dataclass(frozen=True)
class SearchEntry:
    title: str
    page: str  # 页面脚本路径
    breadcrumb: str
    query_params: tuple[tuple[str, str], ...] = ()
    keywords: str = ""
    highlight: str = ""  # 跳转后要定位并高亮的文字，默认用标题
    highlight_context: str = ""  # 同一块里的辅助文字，用来区分同名条目

    @property
    def section(self) -> str:
        return self.breadcrumb.split(" › ")[0]


def _normalize(text: str) -> str:
    return "".join(text.lower().split())


def _str(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _text(node: ast.AST | None) -> str:
    """普通字符串或 f-string 里的纯文本部分。"""
    if isinstance(node, ast.JoinedStr):
        return "".join(_str(part) or "" for part in node.values)
    return _str(node) or ""


def _assignments(path: Path) -> dict[str, ast.expr]:
    """模块顶层的 NAME = value / NAME: type = value。"""
    if not path.exists():
        return {}
    values: dict[str, ast.expr] = {}
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    values[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value:
            values[node.target.id] = node.value
    return values


def _tuples(node: ast.expr | None) -> list[list[ast.expr]]:
    """[(a, b), (c, d)] → [[a, b], [c, d]]"""
    if not isinstance(node, (ast.List, ast.Tuple)):
        return []
    return [elt.elts for elt in node.elts if isinstance(elt, (ast.List, ast.Tuple)) and elt.elts]


def _first_strings(node: ast.expr | None) -> list[str]:
    """[("名称", ...), ...] → ["名称", ...]"""
    return [name for elts in _tuples(node) if (name := _str(elts[0]))]


def _dict_items(node: ast.expr | None) -> list[tuple[str, ast.expr]]:
    if not isinstance(node, ast.Dict):
        return []
    return [(key, value) for key_node, value in zip(node.keys, node.values) if (key := _str(key_node))]


def _pages() -> dict[str, tuple[str, str]]:
    """sephiriadfm05.py 里的 st.Page("pages/x.py", title=..., url_path=...) → {路径: (标题, url_path)}"""
    pages: dict[str, tuple[str, str]] = {}
    for node in ast.walk(ast.parse(MAIN_SCRIPT.read_text(encoding="utf-8"))):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "Page" or not node.args:
            continue
        path = _str(node.args[0])
        options = {kw.arg: _str(kw.value) for kw in node.keywords if kw.arg}
        if path and options.get("title"):
            pages[path] = (options["title"], options.get("url_path") or Path(path).stem)
    return pages


def _category_entries(
    page: str,
    page_title: str,
    categories: ast.expr | None,
    item_param: str,
    authors_node: ast.expr | None,
) -> list[SearchEntry]:
    authors = {name: author for name, value in _dict_items(authors_node) if (author := _str(value))}
    entries = []
    for category, items in _dict_items(categories):
        entries.append(SearchEntry(category, page, page_title, (("category", category),)))
        for item in _first_strings(items):
            author = authors.get(item)
            entries.append(
                SearchEntry(
                    item,
                    page,
                    f"{page_title} › {category}",
                    (("category", category), (item_param, item)),
                    keywords=f"作者：{author}" if author else "",
                )
            )
    return entries


def _build_entries(pages: dict[str, tuple[str, str]]) -> list[SearchEntry]:
    titles = {page: title for page, (title, _) in pages.items() if page != SEARCH_PAGE}
    entries = [SearchEntry(title, page, "站内页面") for page, title in titles.items()]

    def load(page: str) -> tuple[dict[str, ast.expr], str]:
        return _assignments(ROOT_DIR / page), titles.get(page, "")

    # 列表页：[(名称, 图片), ...]，页面用 ?<param>=名称 定位，标题与页面小标题一致
    for page, constant, title_template, param in (
        ("pages/1_weapon_rankings.py", "VERSION_RANKINGS", "{}版本武器排行榜", "version"),
        ("pages/2_weapon_analysis.py", "WEAPONS", "{}全改造一图流", "weapon"),
    ):
        values, page_title = load(page)
        for name in _first_strings(values.get(constant)):
            entries.append(SearchEntry(title_template.format(name), page, page_title, ((param, name),)))

    # 分类页：{大类: [(条目, 文件), ...]}，页面用 ?category=大类&<param>=条目 定位
    for page, constant, param in (
        ("pages/3_build_analysis.py", "BUILD_CATEGORIES", "build"),
        ("pages/4_game_basics.py", "BASIC_CATEGORIES", "item"),
        ("pages/8_attribute_analysis.py", "ATTRIBUTE_CATEGORIES", "item"),
    ):
        values, page_title = load(page)
        entries += _category_entries(page, page_title, values.get(constant), param, values.get("BUILD_AUTHORS"))

    page = "pages/5_presets.py"
    values, page_title = load(page)
    for category, presets in _dict_items(values.get("PRESET_DATA")):
        params = (("category", category),)
        entries.append(SearchEntry(f"{category}预设", page, page_title, params))
        for call in getattr(presets, "elts", []):
            if not isinstance(call, ast.Call):
                continue
            fields = {kw.arg: _str(kw.value) for kw in call.keywords if kw.arg}
            name, subtitle, author = fields.get("name"), fields.get("subtitle"), fields.get("author")
            if not name:
                continue
            entries.append(
                SearchEntry(
                    f"{name}（{subtitle}）" if subtitle else name,
                    page,
                    f"{page_title} › {category}",
                    params,
                    keywords=" · ".join(filter(None, (fields.get("notes"), f"作者：{author}" if author else None))),
                    # 预设卡片上标题和副标题分开显示，同名预设靠副标题区分
                    highlight=name,
                    highlight_context=subtitle or "",
                )
            )

    page = "pages/7_faq_quiz.py"
    values, page_title = load(page)
    for elts in _tuples(values.get("FAQ_ITEMS")):
        question = _text(elts[0])
        answer = _text(elts[1]) if len(elts) > 1 else ""
        if question:
            entries.append(
                SearchEntry(question, page, f"{page_title} › 常见问题", (("entry", "常见问题"),), answer)
            )

    return list(dict.fromkeys(entries))


def _page_url(page: str, pages: dict[str, tuple[str, str]]) -> str:
    return "/" + pages.get(page, ("", Path(page).stem))[1]


def _entry_url(entry: SearchEntry, pages: dict[str, tuple[str, str]]) -> str:
    # hl / hlctx 不影响页面本身，只给侧边栏组件用来滚动到文字位置并高亮
    params = [*entry.query_params, ("hl", entry.highlight or entry.title)]
    if entry.highlight_context:
        params.append(("hlctx", entry.highlight_context))
    return _page_url(entry.page, pages) + "?" + urlencode(params, quote_via=quote)


def _script_safe(text: str) -> str:
    """内联进 <script> 时避免提前闭合标签。"""
    return text.replace("</", "<\\/")


@st.cache_resource(show_spinner=False)
def _index_json() -> str:
    """浏览器端用的索引。t/x/p/i 是预先归一化的 标题/栏目+备注/全拼/首字母，与 JS 里的匹配规则对应。"""
    pages = _pages()
    records = [
        {
            "title": entry.title,
            "breadcrumb": entry.breadcrumb,
            "section": entry.section,
            "url": _entry_url(entry, pages),
            "detail": entry.keywords,
            "t": _normalize(entry.title),
            "x": _normalize(f"{entry.breadcrumb} {entry.keywords}"),
            "p": _normalize("".join(lazy_pinyin(entry.title))),
            "i": _normalize("".join(lazy_pinyin(entry.title, style=Style.FIRST_LETTER))),
        }
        for entry in _build_entries(pages)
    ]
    return _script_safe(json.dumps(records, ensure_ascii=False))


@st.cache_resource(show_spinner=False)
def _fuse_js() -> str:
    return _script_safe(FUSE_JS.read_text(encoding="utf-8"))


_BASE_CSS = """
  html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: "Source Sans Pro", "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
  }
  :root {
    --text: #31333f;
    --muted: rgba(49, 51, 63, 0.6);
    --border: rgba(49, 51, 63, 0.2);
    --link: #0068c9;
    --accent: #ff4b4b;
    --accent-bg: rgba(255, 75, 75, 0.08);
    --mark: rgba(255, 164, 33, 0.3);
    --field-bg: #f0f2f6;
    --sidebar-field-bg: #ffffff;
    --hover: rgba(151, 166, 195, 0.25);
  }
  /* 主题跟随父页面 body[data-theme](由主程序的 JS 根据实际背景亮度探测) */
  html.dark {
    --text: #fafafa;
    --muted: rgba(250, 250, 250, 0.6);
    --border: rgba(250, 250, 250, 0.2);
    --link: #58a6ff;
    --mark: rgba(255, 164, 33, 0.35);
    --field-bg: #262730;
    --sidebar-field-bg: #0e1117;
  }
  body { color: var(--text); }
  mark { background: var(--mark); color: inherit; border-radius: 2px; }
"""

_BASE_JS = """
  var ASCII_ONLY = /^[\\x00-\\x7f]*$/;

  // 模糊匹配只在没有精确结果时兜底（容错字）。中文查标题，字母查全拼；
  // 字母字符集小，阈值放宽会匹配出大量无关条目，所以更严格。
  var FUSE_OPTIONS = { includeScore: true, ignoreLocation: true, ignoreFieldNorm: true };
  var fuseTitle = new Fuse(INDEX, Object.assign({ keys: ["title"], threshold: 0.5 }, FUSE_OPTIONS));
  var fusePinyin = new Fuse(INDEX, Object.assign({ keys: ["p"], threshold: 0.3 }, FUSE_OPTIONS));

  function normalize(text) {
    return text.toLowerCase().replace(/\\s+/g, "");
  }

  function tierScore(q, ascii, item) {
    if (q === item.t) return 1000;
    if (item.t.indexOf(q) === 0) return 900;
    if (item.t.indexOf(q) !== -1) return 800;
    if (ascii && (item.i.indexOf(q) === 0 || item.p.indexOf(q) === 0)) return 700;
    if (ascii && (item.i.indexOf(q) !== -1 || item.p.indexOf(q) !== -1)) return 600;
    if (item.x.indexOf(q) !== -1) return 500;
    return 0;
  }

  // 分级：标题精确/前缀/包含 > 拼音 > 栏目/备注；都没有时才用模糊匹配。同分时标题短的优先。
  function search(term) {
    var q = normalize(term);
    if (!q) return { items: [], fuzzy: false };
    var ascii = ASCII_ONLY.test(q);
    var rows = [];
    INDEX.forEach(function (item, order) {
      var score = tierScore(q, ascii, item);
      if (score) rows.push({ item: item, order: order, score: score });
    });
    var fuzzy = !rows.length && q.length >= (ascii ? 4 : 3);
    if (fuzzy) {
      (ascii ? fusePinyin : fuseTitle).search(q).forEach(function (hit) {
        rows.push({ item: hit.item, order: hit.refIndex, score: 100 * (1 - hit.score) });
      });
    }
    rows.sort(function (a, b) {
      return b.score - a.score || a.item.t.length - b.item.t.length || a.order - b.order;
    });
    return { items: rows.map(function (row) { return row.item; }), fuzzy: fuzzy && rows.length > 0 };
  }

  function escapeHtml(text) {
    return text.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function highlight(text, term) {
    var q = term.trim().toLowerCase();
    if (!q) return escapeHtml(text);
    var lower = text.toLowerCase();
    var out = "", pos = 0, at;
    while ((at = lower.indexOf(q, pos)) !== -1) {
      out += escapeHtml(text.slice(pos, at)) + "<mark>" + escapeHtml(text.slice(at, at + q.length)) + "</mark>";
      pos = at + q.length;
    }
    return out + escapeHtml(text.slice(pos));
  }

  function snippet(text, term) {
    var width = 60;
    var plain = text.replace(/\\[([^\\]]*)\\]\\([^)]*\\)/g, "$1").replace(/\\*\\*/g, "").replace(/\\s+/g, " ").trim();
    if (plain.length <= width) return plain;
    var at = plain.toLowerCase().indexOf(term.trim().toLowerCase());
    var start = at > 0 ? Math.max(0, Math.min(at - Math.floor(width / 3), plain.length - width)) : 0;
    var end = start + width;
    return (start ? "…" : "") + plain.slice(start, end) + (end < plain.length ? "…" : "");
  }

  // components.html 的 iframe 沙箱不允许直接跳转顶层页面（target="_top" 会被拦截），
  // 所以在父页面里临时建一个链接来跳转。
  function navigate(url) {
    try {
      var proxy = parent.document.createElement("a");
      proxy.href = url;
      parent.document.body.appendChild(proxy);
      proxy.click();
      proxy.remove();
    } catch (e) {
      window.open(url, "_blank");
    }
  }

  // 带修饰键的点击交给浏览器（新标签页打开）
  function isPlainClick(event) {
    return event.button === 0 && !(event.metaKey || event.ctrlKey || event.shiftKey || event.altKey);
  }

  function fit() {
    try {
      var h = document.getElementById("app").offsetHeight;
      if (window.frameElement && h > 0) window.frameElement.style.height = h + "px";
    } catch (e) {}
  }

  function applyTheme() {
    try {
      var t = parent.document.body.getAttribute("data-theme");
      document.documentElement.classList.toggle("dark", t === "dark");
    } catch (e) {}
  }
  applyTheme();
  try {
    new MutationObserver(applyTheme).observe(parent.document.body, { attributes: true, attributeFilter: ["data-theme", "class"] });
  } catch (e) {}
  try { new ResizeObserver(fit).observe(document.getElementById("app")); } catch (e) {}
  window.addEventListener("load", fit);
"""


_RESULTS_CSS = """
  #app { padding: 2px 0 12px; }
  .search-bar {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    height: 2.5rem;
    padding: 0 0.75rem;
    border: 1px solid transparent;
    border-radius: 0.5rem;
    background: var(--field-bg);
  }
  .search-bar:focus-within { border-color: var(--accent); }
  .search-bar svg { flex: none; color: var(--muted); }
  .search-bar input {
    flex: 1;
    min-width: 0;
    border: 0;
    outline: 0;
    background: transparent;
    color: var(--text);
    font: inherit;
    font-size: 1rem;
  }
  .pills { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.9rem; }
  .pill {
    font: inherit;
    font-size: 0.875rem;
    color: var(--text);
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.2rem 0.75rem;
    cursor: pointer;
  }
  .pill.active { color: var(--accent); border-color: var(--accent); background: var(--accent-bg); }
  .count { color: var(--muted); font-size: 0.875rem; margin: 0.8rem 0 0.3rem; }
  .result { padding: 0.55rem 0; }
  .crumb { color: var(--muted); font-size: 0.875rem; }
  .title { color: var(--link); font-weight: 600; font-size: 1.05rem; line-height: 1.5; text-decoration: none; }
  .title:hover { text-decoration: underline; }
  .detail { font-size: 0.9rem; line-height: 1.55; margin-top: 0.1rem; }
"""

_RESULTS_BODY = """
  <label class="search-bar">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input id="query" type="search" autocomplete="off" placeholder="例如：冰川、jiandun、jd、暴击" aria-label="搜索关键词">
  </label>
  <div class="pills" id="pills"></div>
  <div class="count" id="count"></div>
  <div id="results"></div>
"""

# 需要注入的变量：INITIAL_QUERY
_RESULTS_JS = """
  var ALL = "全部";
  var input = document.getElementById("query");
  var pillsEl = document.getElementById("pills");
  var countEl = document.getElementById("count");
  var resultsEl = document.getElementById("results");
  var section = ALL;

  var urlTimer = null;
  function syncUrl(q) {
    clearTimeout(urlTimer);
    urlTimer = setTimeout(function () {
      try {
        var url = new URL(parent.location.href);
        if (q) url.searchParams.set("q", q); else url.searchParams.delete("q");
        parent.history.replaceState(parent.history.state, "", url.toString());
      } catch (e) {}
    }, 300);
  }

  function render() {
    var term = input.value;
    var trimmed = term.trim();
    var found = search(term);
    var results = found.items;
    var counts = {};
    var order = [];
    results.forEach(function (item) {
      if (!(item.section in counts)) { counts[item.section] = 0; order.push(item.section); }
      counts[item.section] += 1;
    });
    if (section !== ALL && !(section in counts)) section = ALL;

    pillsEl.innerHTML = results.length
      ? [ALL].concat(order).map(function (name) {
          var n = name === ALL ? results.length : counts[name];
          return '<button type="button" class="pill' + (name === section ? " active" : "") +
            '" data-section="' + escapeHtml(name) + '">' + escapeHtml(name) + " " + n + "</button>";
        }).join("")
      : "";

    var shown = section === ALL ? results : results.filter(function (item) { return item.section === section; });
    countEl.textContent = !trimmed
      ? "输入关键词即可实时筛选，支持中文、拼音、拼音首字母和错字模糊匹配。"
      : !results.length ? "没有找到与「" + trimmed + "」相关的内容，换个关键词或试试拼音。"
      : found.fuzzy ? "没有完全匹配的结果，以下是 " + shown.length + " 条相近内容"
      : "找到 " + shown.length + " 条结果";

    resultsEl.innerHTML = shown.map(function (item) {
      return '<div class="result"><div class="crumb">' + escapeHtml(item.breadcrumb) + "</div>" +
        '<a class="title" target="_top" href="' + escapeHtml(item.url) + '">' + highlight(item.title, term) + "</a>" +
        (item.detail ? '<div class="detail">' + highlight(snippet(item.detail, term), term) + "</div>" : "") +
        "</div>";
    }).join("");

    syncUrl(trimmed);
    fit();
  }

  pillsEl.addEventListener("click", function (event) {
    var button = event.target.closest(".pill");
    if (!button) return;
    section = button.getAttribute("data-section");
    render();
  });
  resultsEl.addEventListener("click", function (event) {
    var link = event.target.closest("a.title");
    if (!link || !isPlainClick(event)) return;
    event.preventDefault();
    navigate(link.href);
  });
  input.addEventListener("input", render);
  input.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.isComposing) input.blur();  // 手机上收起键盘
  });

  input.value = INITIAL_QUERY;
  render();
  if (!INITIAL_QUERY) input.focus({ preventScroll: true });
"""


# 输入框和上方导航链接对齐：同宽、28px 高、6px 圆角、8px 左内边距、14px 字号
_SIDEBAR_CSS = """
  .field {
    display: flex;
    align-items: center;
    box-sizing: border-box;
    height: 28px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--sidebar-field-bg);
  }
  .field:focus-within { border-color: var(--accent); }
  #app.open { padding-bottom: 8px; }  /* 给列表阴影留出位置 */
  .field input {
    flex: 1;
    min-width: 0;
    height: 26px;
    padding: 0 8px;
    border: 0;
    outline: 0;
    background: transparent;
    color: var(--text);
    font: inherit;
    font-size: 14px;
  }
  .field input::placeholder { color: var(--muted); }
  #suggestions {
    display: flex;
    flex-direction: column;
    gap: 2px;
    margin-top: 4px;
    padding: 4px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--sidebar-field-bg);
    box-shadow: 0 6px 12px -6px rgba(0, 0, 0, 0.25);
  }
  #suggestions[hidden] { display: none; }
  .row {
    display: block;
    padding: 3px 8px;
    border-radius: 6px;
    color: var(--text);
    text-decoration: none;
    line-height: 1.4;
  }
  .row:hover, .row.active { background: var(--hover); }
  .row-title, .row-crumb { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .row-title { font-size: 14px; }
  .row-crumb { font-size: 12px; color: var(--muted); }
  .row.all { font-size: 13px; color: var(--link); }
  .empty { padding: 3px 8px; font-size: 13px; color: var(--muted); }
"""

_SIDEBAR_BODY = """
  <div class="field">
    <input id="query" type="text" autocomplete="off" placeholder="搜索（回车查看全部结果）" aria-label="搜索全站">
  </div>
  <div id="suggestions" hidden></div>
"""

# 需要注入的变量：SEARCH_URL
_SIDEBAR_JS = """
  var MAX_SUGGESTIONS = 8;
  var input = document.getElementById("query");
  var listEl = document.getElementById("suggestions");
  var appEl = document.getElementById("app");
  var current = [];
  var active = -1;
  var focused = false;

  function searchPageUrl(q) {
    return SEARCH_URL + "?q=" + encodeURIComponent(q);
  }

  function render() {
    var term = input.value;
    var trimmed = term.trim();
    if (!trimmed || !focused) {
      listEl.hidden = true;
      appEl.classList.remove("open");
      listEl.innerHTML = "";
      current = [];
      active = -1;
      fit();
      return;
    }
    var found = search(term);
    current = found.items.slice(0, MAX_SUGGESTIONS);
    if (active >= current.length) active = -1;
    var rows = current.map(function (item, index) {
      return '<a class="row' + (index === active ? " active" : "") + '" target="_top" href="' + escapeHtml(item.url) + '">' +
        '<span class="row-title">' + highlight(item.title, term) + "</span>" +
        '<span class="row-crumb">' + escapeHtml(item.breadcrumb) + "</span></a>";
    }).join("");
    var footer = found.items.length
      ? '<a class="row all" target="_top" href="' + escapeHtml(searchPageUrl(trimmed)) + '">查看全部 ' +
        found.items.length + (found.fuzzy ? " 条相近结果" : " 条结果") + " →</a>"
      : '<div class="empty">没有找到相关内容</div>';
    listEl.innerHTML = rows + footer;
    listEl.hidden = false;
    appEl.classList.add("open");
    fit();
  }

  input.addEventListener("input", function () { active = -1; render(); });
  input.addEventListener("focus", function () { focused = true; render(); });
  input.addEventListener("blur", function () { focused = false; setTimeout(render, 150); });
  input.addEventListener("keydown", function (event) {
    if (event.isComposing || event.keyCode === 229) return;  // 中文输入法选词时的回车 / 方向键不处理
    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      if (!current.length) return;
      event.preventDefault();
      var n = current.length;
      active = event.key === "ArrowDown" ? (active + 1) % n : (active <= 0 ? n - 1 : active - 1);
      render();
    } else if (event.key === "Enter") {
      var q = input.value.trim();
      if (!q) return;
      event.preventDefault();
      // 用方向键选中了某条就打开它，否则打开「全站搜索」页展示全部结果
      navigate(active >= 0 ? current[active].url : searchPageUrl(q));
    } else if (event.key === "Escape") {
      input.value = "";
      render();
    }
  });
  // 按下时不让输入框失焦，否则列表会在点击生效前收起
  listEl.addEventListener("mousedown", function (event) { event.preventDefault(); });
  listEl.addEventListener("click", function (event) {
    var row = event.target.closest("a.row");
    if (!row || !isPlainClick(event)) return;
    event.preventDefault();
    navigate(row.getAttribute("href"));
  });
  fit();
"""


_JUMP_TO_HIT_JS = """
  // 从搜索结果跳转过来时，网址带 hl=要定位的文字（预设卡片另带 hlctx=副标题，用来区分同名预设）。
  // 侧边栏组件每个页面都会加载，所以由它等页面内容渲染出来后滚动到文字位置并用黄色背景高亮。
  // 高亮用 CSS Custom Highlight API，不改动 Streamlit 管理的 DOM 结构。
  (function jumpToSearchHit() {
    var params;
    try { params = new URL(parent.location.href).searchParams; } catch (e) { return; }
    var text = params.get("hl");
    if (!text) return;
    var context = params.get("hlctx") || "";
    var HIGHLIGHT_NAME = "site-search-hit";
    var HIGHLIGHT_BG = "#ffe066";
    var HIGHLIGHT_FG = "#1f2937";
    var started = Date.now();
    var userScrolled = false;
    ["wheel", "touchstart", "keydown"].forEach(function (type) {
      parent.addEventListener(type, function () { userScrolled = true; }, { once: true, passive: true });
    });

    function isVisible(el) {
      return !!el && el.getClientRects().length > 0;
    }

    // 标题 / 折叠卡片标题最优先，其次是预设卡片，按钮（如分类选择器）上的同名文字只作兜底
    function priority(el, inFrame) {
      if (el.closest("h1, h2, h3, h4, h5, h6, summary")) return 4;
      if (inFrame) return 3;
      if (el.closest("button, [role=tab], label")) return 1;
      return 2;
    }

    function collect(doc, root, frame) {
      var hits = [];
      var walker = doc.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      for (var node = walker.nextNode(); node; node = walker.nextNode()) {
        var at = node.nodeValue.indexOf(text);
        var el = node.parentElement;
        if (at === -1 || !isVisible(el)) continue;
        var card = context ? el.closest(".preset-card") : null;
        hits.push({
          doc: doc, node: node, at: at, el: el, frame: frame,
          priority: priority(el, !!frame),
          inContext: !!card && card.textContent.indexOf(context) !== -1,
        });
      }
      return hits;
    }

    function locate() {
      var root = parent.document.querySelector('[data-testid="stMain"]') || parent.document.body;
      var hits = collect(parent.document, root, null);
      root.querySelectorAll("iframe").forEach(function (frame) {
        try {
          var doc = frame.contentDocument;
          if (doc && doc.body && isVisible(frame)) hits = hits.concat(collect(doc, doc.body, frame));
        } catch (e) {}
      });
      hits.sort(function (a, b) { return (b.inContext - a.inContext) || (b.priority - a.priority); });
      return hits[0] || null;
    }

    function paint(hit) {
      var win = hit.doc.defaultView;
      if (win.CSS && win.CSS.highlights && win.Highlight) {
        if (!hit.doc.getElementById(HIGHLIGHT_NAME)) {
          var style = hit.doc.createElement("style");
          style.id = HIGHLIGHT_NAME;
          style.textContent = "::highlight(" + HIGHLIGHT_NAME + ") { background-color: " + HIGHLIGHT_BG +
            "; color: " + HIGHLIGHT_FG + "; }";
          hit.doc.head.appendChild(style);
        }
        var range = hit.doc.createRange();
        range.setStart(hit.node, hit.at);
        range.setEnd(hit.node, hit.at + text.length);
        win.CSS.highlights.set(HIGHLIGHT_NAME, new win.Highlight(range));
      } else {
        // 旧浏览器不支持 CSS Custom Highlight API：给文字所在元素整体加背景
        hit.el.style.backgroundColor = HIGHLIGHT_BG;
        hit.el.style.color = HIGHLIGHT_FG;
      }
    }

    // 直接跳过去，不用平滑滚动：页面在后台标签页等不可见状态时平滑滚动根本不会执行
    function reveal(hit) {
      (hit.frame || hit.el).scrollIntoView({ block: "center" });
    }

    // 上方的图片、预设卡片加载完会改变页面高度：用户自己滚动之前，内容高度每变一次就重新对准
    function followLayout(hit) {
      var content = parent.document.querySelector('[data-testid="stMainBlockContainer"]');
      if (!content || typeof parent.ResizeObserver === "undefined") return;
      var observer = new parent.ResizeObserver(function () {
        if (userScrolled || !hit.node.isConnected) observer.disconnect();
        else reveal(hit);
      });
      observer.observe(content);
      setTimeout(function () { observer.disconnect(); }, 15000);
    }

    function attempt() {
      var hit = locate();
      var waited = Date.now() - started;
      // 刚加载时标题可能还没渲染出来，先别急着用按钮上的同名文字
      if (!hit || (hit.priority < 3 && waited < 2500)) {
        if (waited < 12000) setTimeout(attempt, 300);
        return;
      }
      paint(hit);
      reveal(hit);
      followLayout(hit);
    }
    attempt();
  })();
"""


def _component_html(page_css: str, page_body: str, page_js: str, **data: str) -> str:
    """组件 iframe 的完整 HTML。data 以同名 JS 全局变量注入（INDEX 总会注入），页面 JS 直接使用。"""
    data_js = "".join(
        f"  var {name} = {_script_safe(json.dumps(value, ensure_ascii=False))};\n" for name, value in data.items()
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<style>{_BASE_CSS}{page_css}</style>
</head>
<body>
<div id="app">{page_body}</div>
<script>
  // Fuse.js 7.x 只发布 CommonJS / ESM 构建，这里给 CommonJS 版提供 module 对象后取出 Fuse
  var module = {{ exports: {{}} }};
{_fuse_js()}
  var Fuse = module.exports;
</script>
<script>
  var INDEX = {_index_json()};
{data_js}{_BASE_JS}{page_js}</script>
</body>
</html>
"""


def render_results(initial_query: str) -> None:
    """「全站搜索」页的搜索框 + 结果列表，筛选全部在浏览器里完成。"""
    html = _component_html(_RESULTS_CSS, _RESULTS_BODY, _RESULTS_JS, INITIAL_QUERY=initial_query)
    # 初始高度只兜底，iframe 内 JS 会按内容精确自适应
    components.html(html, height=600, scrolling=False)


# - 结果列表展开时 iframe 会比所在容器高，要浮在下方侧边栏内容之上，否则会被盖住、点不到
# - 侧边栏收起时渲染的 iframe 可能记住一个很窄的宽度，这里强制跟随侧边栏宽度
_SIDEBAR_IFRAME_CSS = """
<style>
section[data-testid="stSidebar"] .st-key-sidebar_search {
  position: relative;
  z-index: 10;
}
section[data-testid="stSidebar"] .st-key-sidebar_search iframe {
  width: 100% !important;
}
</style>
"""


def render_sidebar_search() -> None:
    """侧边栏搜索框：边输入边在下方列出匹配条目，回车打开「全站搜索」页。"""
    html = _component_html(
        _SIDEBAR_CSS,
        _SIDEBAR_BODY,
        _SIDEBAR_JS + _JUMP_TO_HIT_JS,
        SEARCH_URL=_page_url(SEARCH_PAGE, _pages()),
    )
    st.html(_SIDEBAR_IFRAME_CSS)
    with st.container(key="sidebar_search"):
        components.html(html, height=28, scrolling=False)
