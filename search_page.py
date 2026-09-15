import streamlit as st

import site_search


st.title("全站搜索")
st.caption("赛菲莉娅 Sephiria / 边输入边筛选，支持中文、拼音、拼音首字母和错字模糊匹配")

# 网址 /search?q=冰川 可以直接分享或收藏；之后的输入和筛选都在浏览器里完成
site_search.render_results(st.query_params.get("q", ""))
