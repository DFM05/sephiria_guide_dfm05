from pathlib import Path

import streamlit as st

from wiki_ui import show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "weapon_analysis" / "0.11"

WEAPONS = [
    ("剑盾", "sword_shield.png"),
    ("大剑", "greatsword.png"),
    ("匕首", "dagger.png"),
    ("弩", "crossbow.png"),
    ("武士刀", "katana.png"),
    ("长棍", "staff.png"),
]


st.title("武器解析")
st.caption("赛菲莉娅 Sephiria / 六大武器改造分支")

tabs = st.tabs([weapon_name for weapon_name, _ in WEAPONS])

for tab, (weapon_name, image_name) in zip(tabs, WEAPONS):
    with tab:
        st.subheader(f"{weapon_name}全改造一图流 0.11")
        show_wiki_image(ASSET_DIR / image_name)
