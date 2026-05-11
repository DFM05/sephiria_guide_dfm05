import streamlit as st

from wiki_ui import show_wiki_image


from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
RANKING_DIR = ROOT_DIR / "assets" / "wiki" / "weapon_rankings"
VERSION_DIR = RANKING_DIR / "versions"

VERSION_RANKINGS = [
    ("0.11.6", RANKING_DIR / "0.11.6" / "ranking.png"),
    ("0.10.17", VERSION_DIR / "0_10_17.png"),
    ("0.10.8", VERSION_DIR / "0_10_8.png"),
    ("0.9.8", VERSION_DIR / "0_9_8.png"),
    ("0.9.6", VERSION_DIR / "0_9_6.png"),
    ("0.9正式版", VERSION_DIR / "0_9_release.png"),
    ("0.9测试版", VERSION_DIR / "0_9_beta.png"),
    ("0.8", VERSION_DIR / "0_8.png"),
]


st.title("不同版本武器排行榜")
st.caption("赛菲莉娅 Sephiria / 不同版本武器排行榜")

version = st.segmented_control(
    "选择版本",
    options=[version_name for version_name, _ in VERSION_RANKINGS],
    default="0.11.6",
)

selected_image = next(image_path for version_name, image_path in VERSION_RANKINGS if version_name == version)

st.subheader(f"{version}版本武器排行榜")
show_wiki_image(selected_image)

if version == "0.11.6":
    st.divider()
    st.subheader("详细分析")

    t0_t1_tab, t1_5_tab, t2_t4_tab = st.tabs(
        [
            "T0-T1",
            "T1.5",
            "T2-T4",
        ]
    )

    with t0_t1_tab:
        st.subheader("T0-T1 详细分析")
        show_wiki_image(RANKING_DIR / "0.11.6" / "analysis_t0_t1.png")

    with t1_5_tab:
        st.subheader("T1.5 详细分析")
        show_wiki_image(RANKING_DIR / "0.11.6" / "analysis_t1_5.png")

    with t2_t4_tab:
        st.subheader("T2-T4 详细分析")
        show_wiki_image(RANKING_DIR / "0.11.6" / "analysis_t2_t4.png")
