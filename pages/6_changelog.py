import streamlit as st

# Site update announcements, newest first.
# To publish a new announcement, prepend a new dict here:
# {"date": "YYYY-MM-DD", "items": ["line 1", "line 2", ...]}
UPDATES = [
    {
        "date": "2026-09-13",
        "items": [
            "新分区上线：**面板属性详解**——逐项解析面板上的各类属性（四属性伤害、HP&MP、防御&闪避、暴击、攻速&移速、伤害放大、武器伤害、杂项、流派专属加成）及其数值来源与叠加方式",
            "最近赛菲莉娅迎来了大更新，其余分区的部分内容亟待修改，请耐心等待",
        ],
    },
    {
        "date": "2026-09-01",
        "items": [
            "新分区上线：**常见问题 & 隋唐小测**——常见问题以可展开的问答卡片呈现，隋唐小测包含判断题 / 单选题 / 多选题，答对才会揭晓解析；之后会加更多内容",
        ],
    },
    {
        "date": "2026-08-30",
        "items": [
            "武器排行榜：新增 **1.0.30** 与 **0.12.0** 版本总榜；1.0.30 附「上游 / 中游 / 下游」详细分析（制作中）",
            "流派解析：新增 **武器所属流派索引**（剑盾 / 大剑 / 匕首 / 弩 / 武士刀 / 长棍）",
            "流派解析：物理流派、三元素流派、其他流派全部替换为一图流新版图",
            "流派解析：新增 **单独武器/流派解析** 分区，收录裁判官、内波拉克斯、等离子炙热之刃、图书馆幽灵封印研究会第2型、精灵融合杖伊洛妮卡、书库之阳亚达玛的誓约",
            "预设合集：六大武器预设码全收集完成（共 **162** 张）",
            "全站：各内容页新增「内容最后更新」时间显示",
            "游戏基础/机制分析：标记为施工中，新版内容整理中",
        ],
    },
    {
        "date": "更早",
        "items": [
            "上线不同版本武器排行榜（0.8 ~ 0.11.6，含 0.11.6 三期详细分析）",
            "上线武器解析：六大武器全改造一图流",
            "上线流派解析：各流派词条图解",
            "上线游戏基础/机制分析",
            "上线预设合集与可复制预设码",
        ],
    },
]


st.title("更新公告")
st.caption("赛菲莉娅 Sephiria / 网站内容更新记录")

for index, entry in enumerate(UPDATES):
    is_latest = index == 0
    date_header = f"🆕 {entry['date']}（最新）" if is_latest else f"📅 {entry['date']}"
    lines = "\n".join(f"- {item}" for item in entry["items"])
    with st.container(border=True):
        st.subheader(date_header)
        st.markdown(lines)
