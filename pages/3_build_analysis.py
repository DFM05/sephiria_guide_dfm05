from pathlib import Path
from urllib.parse import quote

import streamlit as st

from wiki_ui import show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "build_analysis"

BUILD_CATEGORIES = {
    "通用连击神器分析": [
        ("风之歌", "wind_song.png"),
        ("精密", "precision.png"),
        ("元素&诅咒&谈判", "element_curse_negotiation.png"),
        ("学院", "academy.png"),
        ("MP补足方法", "mp_supply_methods.png"),
        ("通用增伤", "general_damage_boost.png"),
        ("通用生存&功能", "general_survival_utility.png"),
    ],
    "物理流派": [
        ("坚固", "sturdy.png"),
        ("物理剑盾", "physical_sword_shield.png"),
        ("物理大剑", "physical_greatsword.png"),
        ("物理匕首", "physical_dagger.png"),
        ("物理弩", "physical_crossbow.png"),
        ("物理武士刀", "physical_katana.png"),
        ("物理长棍", "physical_staff.png"),
    ],
    "三元素流派": [
        ("余烬（灼烧）", "ember.png"),
        ("太阳剑", "sun_sword.png"),
        ("冰川（冻伤）", "glacier.png"),
        ("冰霜武具", "frost_armament.png"),
        ("魔法科技（触电）", "magic_tech.png"),
        ("暴风云（乌云）", "storm_cloud.png"),
    ],
    "其他流派": [
        ("同伴", "companion.png"),
        ("行星", "planet.png"),
        ("湖泊", "lake.png"),
        ("固伤", "fixed_damage.png"),
        ("魔法书", "magic_book.png"),
        ("守护", "guardian.png"),
        ("影子", "shadow.png"),
        ("无暴（鹿）坚风", "no_crit_sturdy_wind_song.png"),
        ("无暴（鹿）其他", "no_crit_other.png"),
    ],
}


def build_url(category_name: str, build_name: str | None = None) -> str:
    url = f"/build_analysis?category={quote(category_name)}"
    if build_name is not None:
        url += f"&build={quote(build_name)}"
    return url


def query_value(name: str) -> str | None:
    value = st.query_params.get(name)
    if isinstance(value, list):
        return value[0] if value else None
    return value


def show_navigation_page() -> None:
    st.subheader("导航页")
    st.write("这里汇总了当前流派解析页里的所有大类和条目。")

    for category_name, builds in BUILD_CATEGORIES.items():
        st.markdown(f"### [{category_name}]({build_url(category_name)})")

        if not builds:
            st.caption("暂未加入具体条目。")
            continue

        links = [
            f"[{build_name}]({build_url(category_name, build_name)})"
            for build_name, _ in builds
        ]
        st.markdown(" / ".join(links))


st.title("流派解析")
st.caption("赛菲莉娅 Sephiria / 流派词条解析")

category_options = ["导航页", *BUILD_CATEGORIES.keys()]
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

builds = BUILD_CATEGORIES[category]
requested_build = query_value("build")

st.subheader(category)

if not builds:
    st.info("这个分类下还没有加入具体流派图片，后续可以继续补充。")
else:
    build_options = [build_name for build_name, _ in builds]
    default_build = requested_build if requested_build in build_options else build_options[0]

    build = st.segmented_control(
        "选择条目",
        options=build_options,
        default=default_build,
    )

    image_name = next(image_name for build_name, image_name in builds if build_name == build)

    st.subheader(build)
    show_wiki_image(ASSET_DIR / image_name)
