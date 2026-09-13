from pathlib import Path
from urllib.parse import quote

import streamlit as st

from wiki_ui import show_last_updated, show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "attribute_analysis"


ATTRIBUTE_CATEGORIES = {
    "四属性伤害": [
        ("物理伤害", "elemental_damage/physical.png"),
        ("火焰属性伤害", "elemental_damage/fire.png"),
        ("冰属性伤害", "elemental_damage/ice.png"),
        ("闪电属性伤害", "elemental_damage/lightning.png"),
    ],
    "HP&MP": [
        ("HP&HP偷取", "hp_mp/hp.png"),
        ("MP&MP再生&MP吸收&消耗MP的能力伤害", "hp_mp/mp.png"),
    ],
    "防御力&闪避": [
        ("防御力&荆棘", "defense_evasion/defense.png"),
        ("闪避", "defense_evasion/evasion.png"),
    ],
    "暴击几率&暴击伤害": [
        ("暴击几率", "crit/crit_chance.png"),
        ("暴击伤害", "crit/crit_damage.png"),
    ],
    "攻击速度&移动速度": [
        ("攻击速度", "speed/attack_speed.png"),
        ("移动速度", "speed/movement_speed.png"),
    ],
    "所有伤害放大，无视防御伤害，无视防御": [
        ("所有伤害放大", "damage_amplification/all_damage_boost.png"),
        ("无视防御伤害&无视防御", "damage_amplification/defense_pierce.png"),
    ],
    "武器伤害相关": [
        ("武器伤害", "weapon_damage/weapon_damage.png"),
        ("普通攻击伤害", "weapon_damage/normal_attack.png"),
        ("冲刺攻击伤害", "weapon_damage/dash_attack.png"),
        ("特殊攻击伤害", "weapon_damage/special_attack.png"),
    ],
    "杂项": [
        ("冲刺恢复速度&冲刺次数", "misc/dash_recovery.png"),
        ("谈判力&幸运值&经验值掉落&叶子掉落", "misc/luck_exp.png"),
        ("背包空间&许愿池容量&水果串上限&神器伤害", "misc/inventory.png"),
    ],
    "流派专属加成": [
        ("魔法书相关", "school_bonus/magic_book.png"),
        ("同伴相关", "school_bonus/companion.png"),
        ("行星相关", "school_bonus/planet.png"),
        ("减益效果相关", "school_bonus/debuff.png"),
        ("灼烧相关", "school_bonus/burn.png"),
        ("太阳剑相关", "school_bonus/sun_sword.png"),
        ("冰冻相关", "school_bonus/freeze.png"),
        ("冰霜武具相关", "school_bonus/frost_armament.png"),
        ("触电相关", "school_bonus/shock.png"),
        ("乌云相关", "school_bonus/storm_cloud.png"),
    ],
}


def build_url(category_name: str, item_name: str | None = None) -> str:
    url = f"/attribute_analysis?category={quote(category_name)}"
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
    st.write("这里汇总了当前面板属性详解页里的所有大类和条目。")

    for category_name, items in ATTRIBUTE_CATEGORIES.items():
        st.markdown(f"### [{category_name}]({build_url(category_name)})")

        if not items:
            st.caption("暂未加入具体条目。")
            continue

        links = [
            f"[{item_name}]({build_url(category_name, item_name)})"
            for item_name, _ in items
        ]
        st.markdown(" / ".join(links))


st.title("面板属性详解")
st.caption("赛菲莉娅 Sephiria / 面板属性详解与属性提供来源")
show_last_updated(ASSET_DIR)

category_options = ["导航页", "面板属性详解", *ATTRIBUTE_CATEGORIES.keys()]
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

if category == "面板属性详解":
    st.warning("🚧 本分区内容正在施工整理中，敬请期待。")
    st.stop()

items = ATTRIBUTE_CATEGORIES[category]
requested_item = query_value("item")

st.subheader(category)

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
    image_path = ASSET_DIR / image_name

    st.subheader(item)

    if not image_path.exists():
        st.info("该条目的攻略图片还没录入，敬请期待。")
        st.stop()

    show_wiki_image(image_path)
