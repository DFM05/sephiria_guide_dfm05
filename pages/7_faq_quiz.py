from pathlib import Path
from urllib.parse import quote

import streamlit as st

from wiki_ui import show_last_updated


# Two entries inside this section. Each entry has its own render function
# below, so new content (FAQ entries / quiz questions) can be added later
# without touching the navigation logic.
SECTION_ENTRIES = ["常见问题", "隋唐小测"]


def build_url(entry_name: str) -> str:
    return f"/faq_quiz?entry={quote(entry_name)}"


def query_value(name: str) -> str | None:
    value = st.query_params.get(name)
    if isinstance(value, list):
        return value[0] if value else None
    return value


def show_navigation_page() -> None:
    st.subheader("导航页")
    st.write("这里汇总了常见问题与隋唐小测的所有条目。")

    links = [f"[{entry_name}]({build_url(entry_name)})" for entry_name in SECTION_ENTRIES]
    st.markdown(" / ".join(links))


# FAQ entries: (question, answer). Add new items here — the page renders
# each one as a collapsible card (collapsed = question only).
JUDICATOR_URL = (
    f"/build_analysis?category={quote('单独武器/流派解析')}&build={quote('裁判官')}"
)

FAQ_ITEMS = [
    (
        "混沌伤害是什么？视为所有属性的意思是可以吃到所有属性面板的加成吗？",
        "混沌是一种伤害的类型（与物理、火焰、冰霜、闪电对应），"
        "它属于所有类型的伤害，也就是**同时被视为**物理、火焰、冰霜、闪电伤害。\n\n"
        "首先要明确的一点是：**属性伤害**和**吃不吃属性面板**是两回事。"
        "虽然说大部分属性伤害都吃属性面板，比如灼烧、冻伤、触电，"
        "但也有不吃面板的属性伤害（余烬白神器·玫瑰、冰川白神器·冰戒指、魔法科技白神器·树枝）。\n\n"
        "所以，**造成什么类型的伤害和吃什么属性的关系 = 0**，看的是造成伤害的具体介绍。\n\n"
        f"如果去 [流派解析 → 单独武器/流派解析 → 裁判官]({JUDICATOR_URL})，可以看到更加细致的分析。",
    ),
    (
        "为什么很多物理流派也会使用元素连击的神器？物理也吃元素吗？",
        "是的。**物理也是元素之一**，所以照样可以享受「最高元素伤害增加」的效果。",
    ),
    (
        "火焰眼罩、麒麟的角、冻结的蛋、宝石盔甲这类专属暴击神器，"
        "难道是说这些类型的伤害只能吃到这点暴击加成，吃不到自己面板上的暴击率和暴击伤害吗？",
        "不是的。除了**没有羁绊神器：战术书的同伴**，以及**无视防御伤害**之外，"
        "所有伤害都可以享受自己面板上的暴击率和暴击伤害加成。\n\n"
        "这些专属的暴击率和暴击伤害是**叠加**在原有暴击率和暴击伤害面板之上的。\n\n"
        "举个例子：假设我有 50% 的面板暴击率，同时还有一个麒麟的角（闪电属性伤害暴击率 +30%），"
        "那么我的闪电属性伤害暴击率实际是 **50% + 30% = 80%**。",
    ),
    (
        "关于「行星」的两个问题：属性加成神器有用吗？银河为什么是行星体系的核心？",
        "**Q1：行星造成的属性伤害种类这么多，拿元素系列神器或者多功能腰带这种"
        "可以同时加多个属性的神器是不是很厉害？**\n\n"
        "行星造成的伤害是一个固定的数值，而非受到面板属性伤害的影响，"
        "任何提升面板属性的神器对于行星没有任何作用。\n\n"
        "---\n\n"
        "**Q2：乐谱银河只有加攻击速度的效果啊，为什么是行星体系的核心，这玩意有什么用？**\n\n"
        "要升满级才有效果。效果是武器攻击可以加速行星的攻击速度，对于行星体系极其关键。",
    ),
    (
        "学院连击神器「冥想书」的立即释放所有法术是什么意思？为什么我还是一次只能按一个法术？",
        "冥想书的实际效果是**取消所有法术的释放前摇**"
        "（就是释放时有一个稍微向后顿一下的动作）。\n\n"
        "小法术（火焰魔弹、冰霜魔弹、闪电魔弹）的前摇本身较少，效果不明显；"
        "但是对于其他法术都有较为明显的效果，可以增加移动流畅性，是一个非常优秀的神器。",
    ),
    (
        "第五章任务做完了，写着让我「享受和平」，是主线已经通关完成了吗？",
        "注意：「享受和平」的字体是错误的，这是克里弗给你的幻境。\n\n"
        "在地图上找猫腻破解幻境，即可继续推进剧情。",
    ),
    (
        "名刀「村正」的攻击算作普通攻击吗？可以触发神器「永恒的冬日」吗？",
        "描述是什么造成的就是什么伤害。村正的攻击虽然不消耗 MP，"
        "但仍然算作**特殊攻击**。\n\n"
        "由于「永恒的冬日」只能通过普通攻击触发，所以村正**不能**触发永恒的冬日。",
    ),
    (
        "湖泊连击神器「石纺锤」写的是增加消耗 MP 能力的伤害，"
        "那如果我本来消耗 MP 的能力不消耗 MP 了（比如使用幽灵的魔法书），"
        "还能享受到石纺锤（或消耗 MP 能力伤害增加）的效果吗？",
        "这玩意目前比较迷：**大部分直接消耗 MP 的攻击都可以享受到石纺锤**，"
        "除了湖泊连击的羁绊神器「水之精灵」。\n\n"
        "下面列举一些比较特殊的例子：\n\n"
        "1. **幽灵使用法术书**：可以享受到「消耗 MP 的能力伤害增加」。\n\n"
        "2. **两个满级青铜镜碎片（特殊攻击 MP 消耗为 0）的大剑**：无法享受到"
        "「消耗 MP 的能力伤害增加」。包括召唤紫水晶的拉扎里恩也是相同的互动方式——"
        "本身享受加成，但如果被两个满级的青铜镜碎片变为 0 消耗，就不再享受了。\n\n"
        "3. **吱嘎的脊椎**：虽然是使用 MP 开启特殊普通攻击形态，"
        "但开启之后的普通攻击可以享受到「消耗 MP 的能力伤害增加」的效果；"
        "有趣的是「15 + 50% 防御」的这个附伤效果并不能享受这个加成。"
        "同时，即使拥有两个青铜镜碎片（开启「重新组装」的 MP 消耗为 0），"
        "在开启特殊普通攻击形态的时候仍然可以使普通攻击享受到该加成。",
    ),
    (
        "剩下一个隐藏成就没做完，到底是什么？/ 与佩尔去见树的成就怎么做？",
        "去兔子村右下角的萝卜田，找一个叫「费尔」的 NPC 对话就可以了。",
    ),
]


def show_faq() -> None:
    st.subheader("常见问题")
    st.caption("点击卡片展开查看答案。")

    if not FAQ_ITEMS:
        st.info("📜 常见问题整理中，敬请期待。")
        return

    for question, answer in FAQ_ITEMS:
        with st.expander(f"**{question}**", expanded=False):
            st.markdown(answer)


# Quiz questions. TRUE_FALSE: {question, answer(bool), explanation}.
# MULTIPLE_CHOICE: {question, options(list), answer_index, explanation}.
TRUE_FALSE_QUESTIONS = [
    {
        "question": "没有战术指南书的情况下，拥有麒麟的角并不能使迷你弩炮造成暴击。",
        "answer": False,
        "explanation": (
            "麒麟的角与战术书给同伴带来的暴击暴伤是不一样的（冻结的蛋与火焰眼罩同理）。"
            "战术指南书只是会把你**面板上**的暴击爆伤以一定的比率分给同伴，"
            "但是这些**不显示在面板上**的暴击爆伤不受影响。",
        ),
    },
    {
        "question": "无视防御伤害其实不可以穿透敌怪的超级护甲。",
        "answer": True,
        "explanation": (
            "无视防御伤害确实只是无视敌人的**防御**，但是超级护甲可不惯着你。"
        ),
    },
    {
        "question": (
            "服装「鹿」的减暴击实际上仅影响面板上的暴击率，"
            "所以当我使用傲慢金冠和麒麟的角等不反映在面板上的效果时，"
            "不会被 -90% 暴击率的负面影响。"
        ),
        "answer": False,
        "explanation": (
            "实际上，不显示在面板上的暴击也是**隐形地叠加在面板上**的，"
            "仍然计入自己面板已有的部分。"
        ),
    },
    {
        "question": (
            "虽然怪刀「毫羽」的攻击是远程的，"
            "但是乐谱「风」仍然可以增加它的范围，因为仍然算作近战攻击。"
        ),
        "answer": True,
        "explanation": "确实可以。",
    },
    {
        "question": (
            "当防御为负的时候，服装「鳄鱼」并不会减少玩家的伤害，"
            "因为鳄鱼仅仅转换正的防御所转化的伤害加成。"
        ),
        "answer": False,
        "explanation": "其实仍然会按照负的防御来减少造成的伤害。",
    },
    {
        "question": (
            "虽然说等离子将触电和灼烧合并为了一个减益效果，"
            "但是在红布碎片的计算下，仍然算作两个减益效果，"
            "因为等离子同时造成灼烧和触电两部分的伤害。"
        ),
        "answer": False,
        "explanation": "一个就是一个，来点等离子笑话。",
    },
    {
        "question": (
            "闪电机枪的特殊攻击「饱和」其实可以享受攻速加成，"
            "不过这个加成是直接按照百分比增加到伤害上的，并不会增加频率。"
        ),
        "answer": False,
        "explanation": "没说就是不吃。",
    },
    {
        "question": "裁判官的普通攻击可以享受物理属性面板加成。",
        "answer": True,
        "explanation": (
            "普通攻击仍然基于物理属性造成伤害，只是变为了混沌属性。"
        ),
    },
    {
        "question": (
            "当你持有等离子头盔的时候，如果你的等离子层数为 9 层"
            "（初始 + 电击虫 + 火焰虫），则武器电光一刻的特殊攻击「一闪」"
            "按照描述可以增加 450% 的伤害，所以电光一刻玩等离子流派是极好的。"
        ),
        "answer": False,
        "explanation": (
            "电光一刻的特殊攻击「一闪」仅享受电击虫的层数加成，仅计算触电层数。"
        ),
    },
    {
        "question": (
            "武器「冷冻公鱼」的效果是特殊攻击赋予两次冻伤而不是两层，"
            "所以甚至可以享受蓝爪的效果两次。"
        ),
        "answer": True,
        "explanation": "描述是这么写的，确实。",
    },
    {
        "question": "同伴伤害和所有伤害放大实际处于同一乘区。",
        "answer": True,
        "explanation": "是真的，虎头犯病了。",
    },
    {
        "question": (
            "由于中毒算作减益伤害而不是直接伤害，"
            "所以不能直接给敌人上火焰、冰霜、闪电之触。"
        ),
        "answer": True,
        "explanation": "确实是，减益伤害不可以直接触发三触。",
    },
]

MULTIPLE_CHOICE_QUESTIONS = [
    {
        "question": "以下哪个或哪些神器可以有效地提升裁判官伤口爆炸的伤害？",
        "options": [
            "绝对戒指",
            "兔子村警卫头盔",
            "冰雪藤",
            "中和剂黑",
            "魔法基础",
        ],
        "answer_indices": [0, 1, 2],
        "explanation": (
            "- **绝对戒指**：可以有效提升裁判官伤口爆炸的伤害。\n"
            "- **兔子村警卫头盔**：武器伤害可以增加。\n"
            "- **冰雪藤**：算是裁判官的小核心。\n"
            "- 中和剂黑加的是减益伤害，但裁判官并不享受。\n"
            "- 魔法基础加的是四属性面板，但裁判官不享受。"
        ),
    },
    {
        "question": "以下哪个伤害不可以造成暴击？",
        "options": [
            "行星",
            "灼烧",
            "帕拉斯的卡牌",
            "红色露水",
        ],
        "answer_index": 3,
        "explanation": (
            "**红色露水不能暴击**，不然就自己触发自己了。\n\n"
            "同时，一般来说只要没有特殊说明，伤害都是可以暴击的；"
            "默认的同伴和无视防御伤害算是另外两个特例。"
        ),
    },
    {
        "question": "红色行星观察日志给予行星的额外伤害可以被哪个神器增加？",
        "options": [
            "橡木炭",
            "火焰虫",
            "巨型望远镜",
            "熔岩珠",
        ],
        "answer_index": 2,
        "explanation": (
            "红色行星观察日志写的灼烧的每一跳仅给予一层灼烧一次的伤害，"
            "所以和层数和灼烧速度都没有关系，"
            "反倒是可以享受到**巨型望远镜**的 50% 的加成。"
        ),
    },
]

WRONG_PROMPTS = ["再想想 🤔", "真的吗？🤨", "不对吧 😏"]


def render_true_false(idx: int, q: dict) -> None:
    with st.container(border=True):
        st.markdown(f"**判断题 {idx + 1}**")
        st.write(q["question"])
        choice = st.radio(
            "你的判断",
            ["对", "错"],
            index=None,
            horizontal=True,
            key=f"tf_{idx}",
            label_visibility="collapsed",
        )
        if choice is None:
            return
        if choice == ("对" if q["answer"] else "错"):
            st.success("✅ 答对了！")
            st.markdown(q["explanation"])
        else:
            prompt = WRONG_PROMPTS[(idx + (choice == "对")) % len(WRONG_PROMPTS)]
            st.warning(f"❌ {prompt}")


def render_choice(idx: int, q: dict) -> None:
    multi = "answer_indices" in q
    with st.container(border=True):
        st.markdown(f"**选择题 {idx + 1}（多选）**" if multi else f"**选择题 {idx + 1}**")
        st.write(q["question"])
        labels = [f"{'ABCDE'[i]}．{text}" for i, text in enumerate(q["options"])]
        if multi:
            selected = st.multiselect(
                "选出所有正确答案",
                labels,
                key=f"mc_{idx}",
                label_visibility="collapsed",
            )
            if not selected:
                return
            sel_idx = sorted(labels.index(x) for x in selected)
            if sel_idx == sorted(q["answer_indices"]):
                st.success("✅ 答对了！")
                st.markdown(q["explanation"])
            else:
                prompt = WRONG_PROMPTS[(idx + len(sel_idx)) % len(WRONG_PROMPTS)]
                st.warning(f"❌ {prompt}")
        else:
            choice = st.radio(
                "选择一个答案",
                labels,
                index=None,
                key=f"mc_{idx}",
                label_visibility="collapsed",
            )
            if choice is None:
                return
            selected = labels.index(choice)
            if selected == q["answer_index"]:
                st.success("✅ 答对了！")
                st.markdown(q["explanation"])
            else:
                prompt = WRONG_PROMPTS[(idx + selected) % len(WRONG_PROMPTS)]
                st.warning(f"❌ {prompt}")


def show_quiz() -> None:
    st.subheader("隋唐小测")
    st.caption("关于赛菲莉娅的趣味题目，测测你对游戏有多了解。")

    mode = st.segmented_control("选择题型", ["判断题", "选择题"], default="判断题")

    if mode == "判断题":
        if not TRUE_FALSE_QUESTIONS:
            st.info("✍️ 判断题筹备中，敬请期待。")
            return
        for i, q in enumerate(TRUE_FALSE_QUESTIONS):
            render_true_false(i, q)
    else:
        if not MULTIPLE_CHOICE_QUESTIONS:
            st.info("✍️ 选择题筹备中，敬请期待。")
            return
        for i, q in enumerate(MULTIPLE_CHOICE_QUESTIONS):
            render_choice(i, q)


ENTRY_RENDERERS = {
    "常见问题": show_faq,
    "隋唐小测": show_quiz,
}


st.title("常见问题&隋唐小测")
st.caption("赛菲莉娅 Sephiria / 常见问题与趣味小测")
show_last_updated(Path(__file__))

entry_options = ["导航页", *SECTION_ENTRIES]
requested_entry = query_value("entry")
default_entry = requested_entry if requested_entry in SECTION_ENTRIES else "导航页"

entry = st.segmented_control(
    "选择条目",
    options=entry_options,
    default=default_entry,
)

if entry == "导航页":
    show_navigation_page()
    st.stop()

ENTRY_RENDERERS[entry]()
