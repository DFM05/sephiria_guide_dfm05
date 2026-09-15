import streamlit as st

import site_search


def main() -> None:
    st.markdown(
        """
        <style>
        :root {
          --home-subtitle: #6b7280;
          --home-border: #e5e7eb;
          --home-intro-bg: #fafafa;
          --home-card-bg: #ffffff;
          --home-card-text: #4b5563;
          --home-card-border-hover: #94a3b8;
          --home-card-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
          --home-hint: #2563eb;
        }
        /* 只在 JS 探测出 Streamlit 真正是深色主题时，才切换变量值 */
        body[data-theme="dark"] {
          --home-subtitle: #9ca3af;
          --home-border: #374151;
          --home-intro-bg: #111827;
          --home-card-bg: #1f2937;
          --home-card-text: #cbd5e1;
          --home-card-border-hover: #6b7280;
          --home-card-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
          --home-hint: #60a5fa;
        }
        .main-title {
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            color: var(--home-subtitle);
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
        }
        .intro-box {
            border: 1px solid var(--home-border);
            border-radius: 8px;
            padding: 1.2rem 1.4rem;
            background: var(--home-intro-bg);
            margin-bottom: 1.5rem;
        }
        .section-card {
            border: 1px solid var(--home-border);
            border-radius: 8px;
            padding: 1rem 1.1rem;
            min-height: 140px;
            background: var(--home-card-bg);
        }
        .section-card-link {
            display: block;
            border: 1px solid var(--home-border);
            border-radius: 8px;
            padding: 1rem 1.1rem;
            min-height: 140px;
            background: var(--home-card-bg);
            color: inherit;
            text-decoration: none;
            transition: border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
        }
        .section-card-link:hover {
            border-color: var(--home-card-border-hover);
            box-shadow: var(--home-card-shadow);
            color: inherit;
            text-decoration: none;
            transform: translateY(-1px);
        }
        .section-card h3 {
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .section-card p {
            color: var(--home-card-text);
            margin: 0;
            line-height: 1.7;
        }
        .section-card-link h3 {
            font-size: 1.1rem;
            margin: 0 0 0.5rem 0;
        }
        .section-card-link p {
            color: var(--home-card-text);
            margin: 0;
            line-height: 1.7;
        }
        .card-hint {
            color: var(--home-hint);
            font-size: 0.95rem;
            margin-top: 0.75rem;
        }
        .update-banner {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            border: 1px solid var(--home-border);
            border-radius: 8px;
            padding: 0.7rem 1.1rem;
            background: var(--home-intro-bg);
            color: inherit;
            text-decoration: none;
            margin-bottom: 1.2rem;
            transition: border-color 0.15s ease, box-shadow 0.15s ease;
        }
        .update-banner:hover {
            border-color: var(--home-card-border-hover);
            box-shadow: var(--home-card-shadow);
            color: inherit;
            text-decoration: none;
        }
        .update-banner .banner-badge {
            flex-shrink: 0;
            background: var(--home-hint);
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: 999px;
            padding: 0.15rem 0.7rem;
        }
        .update-banner .banner-text {
            color: var(--home-card-text);
            font-size: 0.98rem;
        }
        .update-banner .banner-go {
            margin-left: auto;
            flex-shrink: 0;
            color: var(--home-hint);
            font-size: 0.95rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <a class="update-banner" href="/changelog" target="_self">
        <span class="banner-badge">公告</span>
        <span class="banner-text">2026-09-13：新分区「面板属性详解」上线，逐项解析属性与来源</span>
        <span class="banner-go">查看更新公告 →</span>
        </a>
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

    site_search.render_search_input(
        "home_search",
        "搜索武器、流派、属性、预设…（支持拼音，回车搜索）",
        icon=":material/search:",
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <a class="section-card-link" href="/weapon_rankings" target="_self">
            <h3>不同版本武器排行榜</h3>
            <p>整理不同版本中的武器强度、排名变化、推荐程度和适用场景。</p>
            <div class="card-hint">查看武器排行榜</div>
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

    col4, col5, col6, col7 = st.columns(4)

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

    with col5:
        st.markdown(
            """
            <a class="section-card-link" href="/presets" target="_self">
            <h3>预设合集</h3>
            <p>收集可直接复制使用的预设码，按武器、流派和玩法方向整理。</p>
            <div class="card-hint">查看可复制预设</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col6:
        st.markdown(
            """
            <a class="section-card-link" href="/faq_quiz" target="_self">
            <h3>常见问题&隋唐小测</h3>
            <p>常见问题解答，以及关于赛菲莉娅的趣味小测验。</p>
            <div class="card-hint">查看常见问题与小测</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with col7:
        st.markdown(
            """
            <a class="section-card-link" href="/attribute_analysis" target="_self">
            <h3>面板属性详解</h3>
            <p>逐项解析面板上的各类属性，以及它们的数值来源与叠加方式。</p>
            <div class="card-hint">查看属性与来源</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.info("后续会继续加入更多页面，用来整理攻略图片、版本资料和专题解析。")


main()
