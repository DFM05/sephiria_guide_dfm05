"""全站搜索。

条目直接用 ast 从各页面源码里的数据常量（BUILD_CATEGORIES、PRESET_DATA 等）解析出来，
不执行页面脚本，所以页面新增内容后搜索索引会自动同步，不需要另外维护一份列表。

用到的开源项目：
- streamlit-searchbox（https://github.com/m-wrzr/streamlit-searchbox）：带自动补全的搜索框组件
- pypinyin（https://github.com/mozillazg/python-pinyin）：拼音 / 拼音首字母搜索
- RapidFuzz（https://github.com/rapidfuzz/RapidFuzz）：容忍错字的模糊匹配
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

import streamlit as st
from pypinyin import Style, lazy_pinyin
from rapidfuzz import fuzz
from streamlit_searchbox import st_searchbox


ROOT_DIR = Path(__file__).resolve().parent
MAIN_SCRIPT = ROOT_DIR / "sephiriadfm05.py"
SEARCH_KEY = "site_search"
MAX_RESULTS = 15
CJK_FUZZY_CUTOFF = 60
ASCII_FUZZY_CUTOFF = 80


@dataclass(frozen=True)
class SearchEntry:
    title: str
    page: str  # 页面脚本路径，直接传给 st.switch_page
    breadcrumb: str
    query_params: tuple[tuple[str, str], ...] = ()
    keywords: str = ""

    @property
    def label(self) -> str:
        return f"{self.title}  ·  {self.breadcrumb}"


@dataclass(frozen=True)
class _IndexedEntry:
    entry: SearchEntry
    title: str
    extra: str
    pinyin: str
    initials: str


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


def _page_titles() -> dict[str, str]:
    """sephiriadfm05.py 里的 st.Page("pages/x.py", title="...") → {路径: 标题}"""
    titles: dict[str, str] = {}
    for node in ast.walk(ast.parse(MAIN_SCRIPT.read_text(encoding="utf-8"))):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "Page" or not node.args:
            continue
        path = _str(node.args[0])
        title = next((_str(kw.value) for kw in node.keywords if kw.arg == "title"), None)
        if path and title:
            titles[path] = title
    return titles


def _category_entries(
    page: str,
    page_title: str,
    categories: ast.expr | None,
    item_param: str,
    authors: dict[str, str] | None = None,
) -> list[SearchEntry]:
    entries = []
    for category, items in _dict_items(categories):
        entries.append(SearchEntry(category, page, page_title, (("category", category),)))
        for item in _first_strings(items):
            entries.append(
                SearchEntry(
                    item,
                    page,
                    f"{page_title} › {category}",
                    (("category", category), (item_param, item)),
                    keywords=(authors or {}).get(item, ""),
                )
            )
    return entries


def _build_entries() -> list[SearchEntry]:
    titles = _page_titles()
    entries = [SearchEntry(title, page, "站内页面") for page, title in titles.items()]

    page = "pages/1_weapon_rankings.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    for version in _first_strings(values.get("VERSION_RANKINGS")):
        entries.append(SearchEntry(f"{version}版本武器排行榜", page, page_title, (("version", version),)))

    page = "pages/2_weapon_analysis.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    for weapon in _first_strings(values.get("WEAPONS")):
        entries.append(SearchEntry(f"{weapon}全改造一图流", page, page_title, (("weapon", weapon),)))

    page = "pages/3_build_analysis.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    authors = {name: author for name, value in _dict_items(values.get("BUILD_AUTHORS")) if (author := _str(value))}
    entries += _category_entries(page, page_title, values.get("BUILD_CATEGORIES"), "build", authors)

    page = "pages/4_game_basics.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    entries += _category_entries(page, page_title, values.get("BASIC_CATEGORIES"), "item")

    page = "pages/8_attribute_analysis.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    entries += _category_entries(page, page_title, values.get("ATTRIBUTE_CATEGORIES"), "item")

    page = "pages/5_presets.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    for category, presets in _dict_items(values.get("PRESET_DATA")):
        params = (("category", category),)
        entries.append(SearchEntry(f"{category}预设", page, page_title, params))
        for call in getattr(presets, "elts", []):
            if not isinstance(call, ast.Call):
                continue
            fields = {kw.arg: _str(kw.value) for kw in call.keywords if kw.arg}
            name, subtitle = fields.get("name"), fields.get("subtitle")
            if not name:
                continue
            entries.append(
                SearchEntry(
                    f"{name}（{subtitle}）" if subtitle else name,
                    page,
                    f"{page_title} › {category}",
                    params,
                    keywords=" ".join(filter(None, (fields.get("notes"), fields.get("author")))),
                )
            )

    page = "pages/7_faq_quiz.py"
    values, page_title = _assignments(ROOT_DIR / page), titles.get(page, "")
    for elts in _tuples(values.get("FAQ_ITEMS")):
        question = _text(elts[0])
        answer = _text(elts[1]) if len(elts) > 1 else ""
        if question:
            entries.append(
                SearchEntry(question, page, f"{page_title} › 常见问题", (("entry", "常见问题"),), answer)
            )

    return list(dict.fromkeys(entries))


@st.cache_resource(show_spinner=False)
def _index() -> list[_IndexedEntry]:
    return [
        _IndexedEntry(
            entry=entry,
            title=_normalize(entry.title),
            extra=_normalize(f"{entry.breadcrumb} {entry.keywords}"),
            pinyin=_normalize("".join(lazy_pinyin(entry.title))),
            initials=_normalize("".join(lazy_pinyin(entry.title, style=Style.FIRST_LETTER))),
        )
        for entry in _build_entries()
    ]


def _score(query: str, item: _IndexedEntry) -> float:
    if query == item.title:
        return 1000
    if item.title.startswith(query):
        return 900
    if query in item.title:
        return 800
    is_ascii = query.isascii()
    if is_ascii and (item.initials.startswith(query) or item.pinyin.startswith(query)):
        return 700
    if is_ascii and (query in item.initials or query in item.pinyin):
        return 600
    if query in item.extra:
        return 500
    if len(query) < 2:
        return 0
    # 纯字母/数字的查询（版本号、拼音）字符集小，放宽阈值会匹配出大量无关条目
    cutoff = ASCII_FUZZY_CUTOFF if is_ascii else CJK_FUZZY_CUTOFF
    score = fuzz.partial_ratio(query, item.title)
    if is_ascii and len(query) >= 4:
        score = max(score, fuzz.partial_ratio(query, item.pinyin))
    return score if score >= cutoff else 0


def search(term: str) -> list[SearchEntry]:
    """按 标题精确/前缀/包含 > 拼音 > 分类/备注 > 模糊匹配 排序，同分时标题短的优先。"""
    query = _normalize(term)
    if not query:
        return []
    scored = [
        (score, len(item.title), order, item.entry)
        for order, item in enumerate(_index())
        if (score := _score(query, item)) > 0
    ]
    scored.sort(key=lambda row: (-row[0], row[1], row[2]))
    return [entry for *_, entry in scored[:MAX_RESULTS]]


def _search_options(term: str) -> list[tuple[str, SearchEntry]]:
    return [(entry.label, entry) for entry in search(term)]


@st.fragment
def render_search_box() -> None:
    """侧边栏搜索框：输入时只重跑这个 fragment，选中结果后带着分类/条目参数跳转到对应页面。"""
    selected = st_searchbox(
        _search_options,
        key=SEARCH_KEY,
        placeholder="搜索（支持拼音）",
        rerun_scope="fragment",
    )
    if selected is None:
        return
    # 清掉组件状态，否则跳转后的页面会再次读到同一个选中值而反复跳转
    del st.session_state[SEARCH_KEY]
    st.switch_page(selected.page, query_params=dict(selected.query_params))
