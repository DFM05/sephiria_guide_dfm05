import base64
import json
from pathlib import Path

import streamlit as st

from wiki_ui import show_last_updated


ROOT_DIR = Path(__file__).resolve().parents[1]
STATIC_DIR = ROOT_DIR / "static"
ICONS_DIR = STATIC_DIR / "weapon_icons"

WEAPON_DATA = json.loads((STATIC_DIR / "weapon_list.json").read_text(encoding="utf-8"))
# Embed every weapon icon as a base64 data URL so the tier list works on any
# Streamlit host regardless of how static files are routed (/static/ vs
# /app/static/). Total payload is ~150KB for 104 small icons.
for w in WEAPON_DATA:
    icon_path = ICONS_DIR / f"{w['id']}.png"
    if icon_path.exists():
        b64 = base64.b64encode(icon_path.read_bytes()).decode("ascii")
        w["icon"] = f"data:image/png;base64,{b64}"

TIERLIST_HTML = (STATIC_DIR / "tierlist.html").read_text(encoding="utf-8").replace(
    "<script>",
    f"<script>\nwindow.WEAPON_DATA = {json.dumps(WEAPON_DATA, ensure_ascii=False)};",
    1,
)


st.title("制作自己的武器排行榜")
st.caption("赛菲莉娅 Sephiria / 拖拽武器到各等级，制作属于你的排行榜")
st.info("💡 推荐电脑端访问，拖拽体验更佳")
show_last_updated(STATIC_DIR / "weapon_icons")

st.markdown(
    "拖拽下方武器到各等级行，可编辑等级名、添加或删除等级。"
    "完成后点击「导出截图」保存你的排行榜。"
)

st.iframe(TIERLIST_HTML, height="content")
