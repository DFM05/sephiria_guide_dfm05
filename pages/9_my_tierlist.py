from pathlib import Path

import streamlit as st

from wiki_ui import show_last_updated


ROOT_DIR = Path(__file__).resolve().parents[1]
STATIC_DIR = ROOT_DIR / "static"
TIERLIST_HTML = (STATIC_DIR / "tierlist.html").read_text(encoding="utf-8")


st.title("制作自己的武器排行榜")
st.caption("赛菲莉娅 Sephiria / 拖拽武器到各等级，制作属于你的排行榜")
show_last_updated(STATIC_DIR / "weapon_icons")

st.markdown(
    "拖拽下方武器到各等级行，可编辑等级名、添加或删除等级。"
    "完成后点击「导出截图」保存你的排行榜。"
)

st.iframe(TIERLIST_HTML, height="content")
