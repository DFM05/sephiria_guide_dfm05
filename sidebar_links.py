import streamlit as st


BILIBILI_URL = "https://space.bilibili.com/362725513"


def show_sidebar_links() -> None:
    with st.sidebar:
        st.markdown("---")
        st.caption("作者主页")
        st.markdown("B站 DFM05，赛菲莉娅攻略图与资料整理。")
        st.markdown("赛菲莉娅同好联机交流群：1022174074")
        st.link_button("前往作者B站主页", BILIBILI_URL)
