import streamlit as st

from sidebar_links import show_sidebar_links


st.set_page_config(
    page_title="赛菲莉娅 Sephiria 攻略站",
    page_icon="S",
    layout="wide",
)

show_sidebar_links()

navigation = st.navigation(
    [
        st.Page("home_page.py", title="主页", url_path="home"),
        st.Page("pages/1_weapon_rankings.py", title="武器排行榜", url_path="weapon_rankings"),
        st.Page("pages/2_weapon_analysis.py", title="武器解析", url_path="weapon_analysis"),
        st.Page("pages/4_game_basics.py", title="游戏基础/机制分析", url_path="game_basics"),
        st.Page("pages/3_build_analysis.py", title="流派解析", url_path="build_analysis"),
    ]
)

navigation.run()
