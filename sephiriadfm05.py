import streamlit as st

from sidebar_links import show_sidebar_links


st.set_page_config(
    page_title="赛菲莉娅 Sephiria 攻略站",
    page_icon="S",
    layout="wide",
)


def _inject_global_theme_overrides() -> None:
    """全站注入：
    1) 运行一小段 JS，根据 Streamlit 实际渲染的背景色给 <body> 打 data-theme="dark" / "light" 标记
       （不依赖 prefers-color-scheme，避免「OS深色 + 用户手动切Light」的错配）
    2) 对 Streamlit 原生 alert / expander / code 等只在 data-theme="dark" 时做深色覆盖。
    """
    st.markdown(
        """
        <style>
        /* 所有自定义样式的深色覆盖，统一只认 body[data-theme="dark"] */
        body[data-theme="dark"] {
          color-scheme: dark;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stAlert[data-testid="stAlert"] {
          background: #0b2545 !important;
          border-color: #1e3a8a !important;
          color: #bfdbfe !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stAlert[data-testid="stAlert"] p,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stAlert[data-testid="stAlert"] li,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stAlert[data-testid="stAlert"] span {
          color: #bfdbfe !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stSuccess[data-testid="stSuccess"] {
          background: #052e1b !important;
          border-color: #14532d !important;
          color: #bbf7d0 !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stSuccess[data-testid="stSuccess"] p,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stSuccess[data-testid="stSuccess"] li,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stSuccess[data-testid="stSuccess"] span {
          color: #bbf7d0 !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stWarning[data-testid="stWarning"] {
          background: #422006 !important;
          border-color: #78350f !important;
          color: #fde68a !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stWarning[data-testid="stWarning"] p,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stWarning[data-testid="stWarning"] li,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stWarning[data-testid="stWarning"] span {
          color: #fde68a !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stError[data-testid="stError"] {
          background: #450a0a !important;
          border-color: #7f1d1d !important;
          color: #fecaca !important;
        }
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stError[data-testid="stError"] p,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stError[data-testid="stError"] li,
        body[data-theme="dark"] div[data-testid="stAlertContainer"] .stError[data-testid="stError"] span {
          color: #fecaca !important;
        }
        body[data-theme="dark"] div[data-testid="stExpander"] details {
          border-color: #374151 !important;
          background-color: #111827 !important;
        }
        body[data-theme="dark"] div[data-testid="stExpander"] details summary {
          background-color: #111827 !important;
        }
        body[data-theme="dark"] div[data-testid="stCodeBlock"] pre {
          background: #020617 !important;
          color: #e2e8f0 !important;
        }
        body[data-theme="dark"] small,
        body[data-theme="dark"] .stCaption,
        body[data-theme="dark"] [data-testid="stCaptionContainer"] {
          color: #cbd5e1 !important;
        }
        </style>

        <script>
        (function() {
          // 根据 Streamlit 实际生效的背景色，给 <body> 加 data-theme="dark" / "light"。
          // 比 prefers-color-scheme 更可靠：即便 OS 深色 + 用户手动切成 Light，也能正确识别为 Light。
          function detectTheme() {
            var el = document.querySelector('[data-testid="stAppViewContainer"]')
                    || document.querySelector('[data-testid="stApp"]')
                    || document.body;
            var bg = window.getComputedStyle(el).backgroundColor || '';
            var match = bg.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/i);
            if (!match) return null;
            var r = parseInt(match[1], 10), g = parseInt(match[2], 10), b = parseInt(match[3], 10);
            var lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
            return lum < 0.5 ? "dark" : "light";
          }
          function apply() {
            var t = detectTheme();
            if (t && document.body.getAttribute('data-theme') !== t) {
              document.body.setAttribute('data-theme', t);
            }
          }
          apply();
          // Streamlit 切主题会重新渲染但不一定整页 reload，轮询兜底
          var observerAvailable = false;
          if (typeof MutationObserver !== 'undefined') {
            observerAvailable = true;
            var obs = new MutationObserver(function() { apply(); });
            obs.observe(document.documentElement, { attributes: true, subtree: true, attributeFilter: ['class', 'style', 'data-testid'] });
          }
          setInterval(apply, 1200);
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )


_inject_global_theme_overrides()

navigation = st.navigation(
    [
        st.Page("home_page.py", title="主页", url_path="home"),
        st.Page("pages/1_weapon_rankings.py", title="武器排行榜", url_path="weapon_rankings"),
        st.Page("pages/2_weapon_analysis.py", title="武器解析", url_path="weapon_analysis"),
        st.Page("pages/4_game_basics.py", title="游戏基础/机制分析", url_path="game_basics"),
        st.Page("pages/3_build_analysis.py", title="流派解析", url_path="build_analysis"),
        st.Page("pages/5_presets.py", title="预设合集", url_path="presets"),
        st.Page("pages/6_changelog.py", title="更新公告", url_path="changelog"),
    ]
)

# NOTE: st.Page / st.navigation 新 API 下，Streamlit 会在调用 navigation.run()
# 时重新构建整个 sidebar（包含导航链接）。在此之前写的 st.sidebar 内容会被
# 覆盖/丢弃，因此共享侧边栏内容（作者主页、交流群、B站链接等）必须放到
# navigation.run() 之后调用才会稳定显示在导航链接下方。
navigation.run()
show_sidebar_links()
