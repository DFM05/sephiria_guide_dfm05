from pathlib import Path

import streamlit as st

from wiki_ui import show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "build_analysis"

BUILDS = [
    ("固伤流派", "fixed_damage.png"),
    ("余烬流派", "ember.png"),
]


st.title("流派解析")
st.caption("赛菲莉娅 Sephiria / 流派词条解析")

tabs = st.tabs([build_name for build_name, _ in BUILDS])

for tab, (build_name, image_name) in zip(tabs, BUILDS):
    with tab:
        st.subheader(build_name)
        show_wiki_image(ASSET_DIR / image_name)
