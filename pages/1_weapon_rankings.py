import streamlit as st

from wiki_ui import show_last_updated, show_wiki_image


from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
RANKING_DIR = ROOT_DIR / "assets" / "wiki" / "weapon_rankings"
VERSION_DIR = RANKING_DIR / "versions"

VERSION_RANKINGS = [
    ("1.0.30", RANKING_DIR / "1.0.30" / "ranking.png"),
    ("0.12.0", RANKING_DIR / "0.12.0" / "ranking.png"),
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
show_last_updated(RANKING_DIR)

version_options = [version_name for version_name, _ in VERSION_RANKINGS]
requested_version = st.query_params.get("version")

version = st.segmented_control(
    "选择版本",
    options=version_options,
    default=requested_version if requested_version in version_options else "1.0.30",
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

elif version == "1.0.30":
    st.divider()
    st.subheader("详细分析")

    analysis_tabs = st.tabs(["上游", "中游", "下游"])
    analysis_keys = ["upstream", "midstream", "downstream"]

    # Detailed analysis images are still being produced; render them once they
    # are synced into assets/wiki/weapon_rankings/1.0.30/.
    for tab, tab_key in zip(analysis_tabs, analysis_keys):
        with tab:
            analysis_path = RANKING_DIR / "1.0.30" / f"analysis_{tab_key}.png"
            if analysis_path.exists():
                show_wiki_image(analysis_path)
            else:
                st.info("该部分的详细分析图还在制作中，敬请期待。")
