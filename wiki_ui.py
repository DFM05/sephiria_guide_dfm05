import base64
import html as html_lib
import json
from datetime import datetime
from pathlib import Path
from typing import Iterable

import streamlit as st


def show_wiki_image(image_path: Path, width_ratio: float = 0.8) -> None:
    main_col, spacer_col = st.columns([width_ratio, 1 - width_ratio])

    with main_col:
        st.image(image_path, width="stretch")


def show_last_updated(*roots: Path | str) -> None:
    """Show a caption with the most recent file modification time under the given roots.

    Used as an automatic "content last updated" hint: sync_assets rewrites tracked
    files whenever their source changes, so the newest mtime under a page's asset
    directory is a good proxy for when the page content actually changed.
    """
    latest: float | None = None
    for root in roots:
        root_path = Path(root)
        if root_path.is_file():
            candidates: list[Path] = [root_path]
        elif root_path.is_dir():
            candidates = [p for p in root_path.rglob("*") if p.is_file()]
        else:
            continue
        for path in candidates:
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            if latest is None or mtime > latest:
                latest = mtime

    if latest is not None:
        stamp = datetime.fromtimestamp(latest).strftime("%Y-%m-%d %H:%M")
        st.caption(f"📅 内容最后更新：{stamp}")


_PRESET_CARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<style>
  html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: "Source Sans Pro", "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
  }
  :root {
    --card-bg: #ffffff;
    --card-border: #e5e7eb;
    --icon-bg: #f3f4f6;
    --icon-fg: #9ca3af;
    --text: #111827;
    --text-sub: #4b5563;
    --text-muted: #6b7280;
    --code-label: #6b7280;
    --copy-bg: #f1f5f9;
    --copy-border: #e2e8f0;
    --copy-fg: #334155;
    --copy-bg-hover: #e2e8f0;
    --copy-border-hover: #cbd5e1;
    --copy-fg-hover: #0f172a;
    --copy-copied-bg: #dcfce7;
    --copy-copied-border: #bbf7d0;
    --copy-copied-fg: #166534;
    --copy-error-bg: #fee2e2;
    --copy-error-border: #fecaca;
    --copy-error-fg: #991b1b;
    --code-bg: #0f172a;
    --code-fg: #e2e8f0;
  }
  /* 主题跟随父页面 body[data-theme](由主程序的 JS 根据实际背景亮度探测) */
  html.dark {
    --card-bg: #1f2937;
    --card-border: #374151;
    --icon-bg: #111827;
    --icon-fg: #6b7280;
    --text: #f9fafb;
    --text-sub: #cbd5e1;
    --text-muted: #9ca3af;
    --code-label: #9ca3af;
    --copy-bg: #1e293b;
    --copy-border: #334155;
    --copy-fg: #e2e8f0;
    --copy-bg-hover: #334155;
    --copy-border-hover: #475569;
    --copy-fg-hover: #f8fafc;
    --copy-copied-bg: #064e3b;
    --copy-copied-border: #065f46;
    --copy-copied-fg: #a7f3d0;
    --copy-error-bg: #450a0a;
    --copy-error-border: #7f1d1d;
    --copy-error-fg: #fecaca;
    --code-bg: #020617;
    --code-fg: #e2e8f0;
  }
  .preset-card {
    display: flex;
    gap: 1rem;
    padding: 1rem 1.1rem;
    border: 1px solid var(--card-border);
    border-radius: 10px;
    background: var(--card-bg);
    box-sizing: border-box;
  }
  .preset-card-icon {
    flex: 0 0 96px;
    width: 96px;
    height: 96px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--card-border);
    background: var(--icon-bg);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--icon-fg);
    font-size: 2.4rem;
    font-weight: 700;
  }
  .preset-card-icon img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
  .preset-card-body {
    flex: 1 1 auto;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }
  .preset-card-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0;
    color: var(--text);
    line-height: 1.35;
  }
  .preset-card-subtitle {
    font-size: 0.95rem;
    margin: 0;
    color: var(--text-sub);
    line-height: 1.45;
  }
  .preset-card-notes {
    color: var(--text-muted);
    font-size: 0.88rem;
  }
  .preset-card-meta {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-top: 0.1rem;
  }
  .preset-code-wrap {
    margin-top: 0.55rem;
  }
  .preset-code-label-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.3rem;
  }
  .preset-code-label {
    font-size: 0.8rem;
    color: var(--code-label);
  }
  .preset-copy-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.76rem;
    font-family: inherit;
    color: var(--copy-fg);
    background: var(--copy-bg);
    border: 1px solid var(--copy-border);
    border-radius: 6px;
    padding: 0.2rem 0.55rem;
    cursor: pointer;
    line-height: 1.2;
    transition: background 0.12s ease, border-color 0.12s ease, color 0.12s ease;
    user-select: none;
  }
  .preset-copy-btn:hover {
    background: var(--copy-bg-hover);
    border-color: var(--copy-border-hover);
    color: var(--copy-fg-hover);
  }
  .preset-copy-btn.is-copied {
    background: var(--copy-copied-bg);
    border-color: var(--copy-copied-border);
    color: var(--copy-copied-fg);
  }
  .preset-copy-btn.is-error {
    background: var(--copy-error-bg);
    border-color: var(--copy-error-border);
    color: var(--copy-error-fg);
  }
  .preset-code-box {
    background: var(--code-bg);
    color: var(--code-fg);
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.78rem;
    line-height: 1.55;
    max-height: 9em;
    overflow: auto;
    white-space: normal;
    word-break: break-all;
  }
</style>
</head>
<body>
<div class="preset-card" id="card">
  <div class="preset-card-icon">__ICON_HTML__</div>
  <div class="preset-card-body">
    <p class="preset-card-title">__TITLE__</p>
    __SUBTITLE_HTML__
    __META_HTML__
    <div class="preset-code-wrap">
      <div class="preset-code-label-row">
        <span class="preset-code-label">预设码</span>
        <button type="button" class="preset-copy-btn" id="copyBtn">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span class="preset-copy-label">复制</span>
        </button>
      </div>
      <div class="preset-code-box">__CODE_HTML__</div>
    </div>
  </div>
</div>
<script>
  var CODE = __CODE_JSON__;
  var btn = document.getElementById('copyBtn');
  var label = btn.querySelector('.preset-copy-label');
  var resetTimer = null;

  function applyTheme() {
    try {
      var t = parent.document.body.getAttribute('data-theme');
      document.documentElement.classList.toggle('dark', t === 'dark');
    } catch (e) {}
  }
  applyTheme();
  try {
    new MutationObserver(applyTheme).observe(parent.document.body, {
      attributes: true,
      attributeFilter: ['data-theme', 'class'],
    });
  } catch (e) {}

  function finish(ok) {
    btn.classList.remove('is-copied', 'is-error');
    btn.classList.add(ok ? 'is-copied' : 'is-error');
    label.textContent = ok ? '已复制' : '复制失败';
    if (resetTimer) clearTimeout(resetTimer);
    resetTimer = setTimeout(function () {
      btn.classList.remove('is-copied', 'is-error');
      label.textContent = '复制';
    }, 1500);
  }

  function fallbackCopy() {
    var ta = document.createElement('textarea');
    ta.value = CODE;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    finish(ok);
  }

  btn.addEventListener('click', function () {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(CODE).then(
        function () { finish(true); },
        fallbackCopy
      );
    } else {
      fallbackCopy();
    }
  });

  // iframe height is auto-measured by st.iframe(height="content")
</script>
</body>
</html>
"""


def _build_preset_card_html(
    name: str,
    subtitle: str,
    preset_code: str,
    *,
    icon_html: str,
    notes: str | None,
    author: str | None,
    version: str | None,
) -> str:
    if notes:
        subtitle_html = (
            f'<p class="preset-card-subtitle">{html_lib.escape(subtitle)}<br>'
            f'<span class="preset-card-notes">{html_lib.escape(notes)}</span></p>'
        )
    else:
        subtitle_html = f'<p class="preset-card-subtitle">{html_lib.escape(subtitle)}</p>'

    meta_parts = []
    if version:
        meta_parts.append(f"版本:{html_lib.escape(version)}")
    if author:
        meta_parts.append(f"作者:{html_lib.escape(author)}")
    meta_html = (
        f'<div class="preset-card-meta">{" · ".join(meta_parts)}</div>'
        if meta_parts
        else ""
    )

    card_html = _PRESET_CARD_TEMPLATE
    card_html = card_html.replace("__ICON_HTML__", icon_html)
    card_html = card_html.replace("__TITLE__", html_lib.escape(name))
    card_html = card_html.replace("__SUBTITLE_HTML__", subtitle_html)
    card_html = card_html.replace("__META_HTML__", meta_html)
    card_html = card_html.replace("__CODE_HTML__", html_lib.escape(preset_code))
    card_html = card_html.replace("__CODE_JSON__", json.dumps(preset_code, ensure_ascii=False))
    return card_html


def render_preset_card(
    name: str,
    subtitle: str,
    preset_code: str,
    *,
    icon_path: Path | str | None = None,
    icon_text: str | None = None,
    author: str | None = None,
    version: str | None = None,
    notes: str | None = None,
) -> None:
    icon_html = ""
    if icon_path:
        resolved = Path(icon_path)
        if resolved.exists():
            try:
                b64 = base64.b64encode(resolved.read_bytes()).decode("ascii")
                suffix = resolved.suffix.lower().lstrip(".") or "png"
                mime = "image/" + ("svg+xml" if suffix == "svg" else suffix)
                icon_html = (
                    f'<img src="data:{mime};base64,{b64}" alt="{html_lib.escape(name)}" />'
                )
            except OSError:
                icon_html = ""
        if not icon_html:
            icon_html = html_lib.escape(icon_text or name[:1] or "?")
    else:
        icon_html = html_lib.escape(icon_text or name[:1] or "?")

    card_html = _build_preset_card_html(
        name,
        subtitle,
        preset_code,
        icon_html=icon_html,
        notes=notes,
        author=author,
        version=version,
    )
    # st.iframe with height="content" auto-measures the card height
    st.iframe(card_html, height="content")


def render_preset_grid(
    presets: Iterable[dict],
    *,
    columns: int = 2,
) -> None:
    presets = list(presets)
    if not presets:
        st.info("这个分类下还没有预设，后续可以继续补充。")
        return

    for chunk_start in range(0, len(presets), columns):
        chunk = presets[chunk_start : chunk_start + columns]
        cols = st.columns(columns)
        for col, preset in zip(cols, chunk):
            with col:
                render_preset_card(**preset)
