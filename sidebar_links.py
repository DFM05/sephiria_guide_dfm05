import streamlit as st


BILIBILI_URL = "https://space.bilibili.com/362725513"


def show_sidebar_links() -> None:
    with st.sidebar:
        st.markdown("---")
        st.caption("作者主页")
        st.link_button("前往作者B站主页", BILIBILI_URL, use_container_width=True)
        st.markdown("有网站相关的问题或建议，可以通过 B 站私信联系作者。")
        st.markdown(
            "赛菲莉娅同好联机交流群（QQ）：\n"
            "- 一群：`1022174074`（群已满）\n"
            "- 二群：`992536561`\n"
            "- 粉丝群：`1104938832`　专注于赛菲莉娅原版讨论，之后的网页更新预计也会在这个群里发布"
        )
