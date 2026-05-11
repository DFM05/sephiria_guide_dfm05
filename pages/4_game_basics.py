from pathlib import Path
from urllib.parse import quote

import streamlit as st

from wiki_ui import show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "game_basics"


BASIC_CATEGORIES = {
    "神器&石板解锁": [
        ("初始神器", "unlocks/initial_artifacts.png"),
        ("非初始神器&解锁方法（待补全）", "unlocks/non_initial_artifacts_unlocks.png"),
        ("命运刻印解锁神器", "unlocks/fate_mark_artifacts.png"),
        ("击败boss物品解锁（待补全）", "unlocks/boss_drop_unlocks.png"),
        ("石板&非初始石板解锁（待补全）", "unlocks/tablets_unlocks.png"),
    ],
    "游戏基础": [
        ("天赋（才能）", "basics/talent.png"),
        ("奇迹（树根）", "basics/miracle_root.png"),
    ],
}


def build_url(category_name: str, item_name: str | None = None) -> str:
    url = f"/game_basics?category={quote(category_name)}"
    if item_name is not None:
        url += f"&item={quote(item_name)}"
    return url


def query_value(name: str) -> str | None:
    value = st.query_params.get(name)
    if isinstance(value, list):
        return value[0] if value else None
    return value


def show_navigation_page() -> None:
    st.subheader("导航页")
    st.write("这里汇总了当前游戏基础/机制分析页里的所有大类和条目。")

    for category_name, items in BASIC_CATEGORIES.items():
        st.markdown(f"### [{category_name}]({build_url(category_name)})")

        if not items:
            st.caption("暂未加入具体条目。")
            continue

        links = [
            f"[{item_name}]({build_url(category_name, item_name)})"
            for item_name, _ in items
        ]
        st.markdown(" / ".join(links))


st.title("游戏基础/机制分析")
st.caption("赛菲莉娅 Sephiria / 游戏基础与机制整理")

category_options = ["导航页", *BASIC_CATEGORIES.keys()]
requested_category = query_value("category")
default_category = requested_category if requested_category in category_options else "导航页"

category = st.segmented_control(
    "选择大类",
    options=category_options,
    default=default_category,
)

if category == "导航页":
    show_navigation_page()
    st.stop()

st.subheader(category)

items = BASIC_CATEGORIES[category]
requested_item = query_value("item")

if not items:
    st.info("这个分类下还没有加入具体内容，后续可以继续补充。")
else:
    item_options = [item_name for item_name, _ in items]
    default_item = requested_item if requested_item in item_options else item_options[0]

    item = st.segmented_control(
        "选择条目",
        options=item_options,
        default=default_item,
    )

    image_name = next(image_name for item_name, image_name in items if item_name == item)

    st.subheader(item)
    show_wiki_image(ASSET_DIR / image_name)
