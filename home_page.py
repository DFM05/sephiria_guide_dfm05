import streamlit as st


def main() -> None:
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            color: #6b7280;
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
        }
        .intro-box {
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 1.2rem 1.4rem;
            background: #fafafa;
            margin-bottom: 1.5rem;
        }
        .section-card {
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 1rem 1.1rem;
            min-height: 140px;
            background: #ffffff;
        }
        .section-card-link {
            display: block;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 1rem 1.1rem;
            min-height: 140px;
            background: #ffffff;
            color: inherit;
            text-decoration: none;
            transition: border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
        }
        .section-card-link:hover {
            border-color: #94a3b8;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
            color: inherit;
            text-decoration: none;
            transform: translateY(-1px);
        }
        .section-card h3 {
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .section-card p {
            color: #4b5563;
            margin: 0;
            line-height: 1.7;
        }
        .section-card-link h3 {
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .section-card-link p {
            color: #4b5563;
            margin: 0;
            line-height: 1.7;
        }
        .card-hint {
            color: #2563eb;
            font-size: 0.95rem;
            margin-top: 0.75rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main-title">赛菲莉娅 Sephiria 攻略站</div>
        <div class="subtitle">B站 DFM05 独立制作的游戏攻略资料站</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="intro-box">
        这是由 <strong>B站 DFM05</strong> 独立制作的关于游戏
        <strong>赛菲莉娅（Sephiria）</strong> 的攻略资料站。
        <br><br>
        本站内容包括但不限于不同版本武器排行榜、武器解析，
        以及各种游戏机制解析。
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("内容分类")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <a class="section-card-link" href="/weapon_rankings" target="_self">
            <h3>不同版本武器排行榜</h3>
            <p>整理不同版本中的武器强度、排名变化、推荐程度和适用场景。</p>
            <div class="card-hint">查看 0.11.6版本武器排行榜</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <a class="section-card-link" href="/weapon_analysis" target="_self">
            <h3>武器解析</h3>
            <p>记录武器机制、优缺点、使用思路、搭配方向和实战表现。</p>
            <div class="card-hint">查看六大武器改造分支</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <a class="section-card-link" href="/game_basics" target="_self">
            <h3>游戏基础/机制分析</h3>
            <p>汇总游戏内的重要机制、隐藏规则、数值逻辑和常见问题。</p>
            <div class="card-hint">查看基础与机制内容</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <a class="section-card-link" href="/build_analysis" target="_self">
            <h3>流派解析</h3>
            <p>整理不同流派的核心思路、关键武器、常用搭配和成型路线。</p>
            <div class="card-hint">查看各大流派解析</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.info("后续会继续加入更多页面，用来整理攻略图片、版本资料和专题解析。")


main()
