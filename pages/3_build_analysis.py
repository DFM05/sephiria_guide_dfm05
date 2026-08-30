from pathlib import Path
from urllib.parse import quote
import shutil

import streamlit as st

from wiki_ui import show_last_updated, show_wiki_image


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets" / "wiki" / "build_analysis"
STATIC_ROOT = Path(__file__).resolve().parents[1] / "static"

# Per-entry author metadata for PDFs in "单独武器/流派解析". Used to render
# a small "作者：@xxx" line right under the sub-header, matching the screenshot
# annotation the user placed next to the build title.
BUILD_AUTHORS: dict[str, str] = {
    "内波拉克斯": "Eden_T",
    "等离子炙热之刃": "小林家今天の饭",
    "图书馆幽灵封印研究会第2型": "梅子黄时雨",
    "裁判官": "DFM05",
    "精灵融合杖伊洛妮卡": "DFM05",
    "书库之阳亚达玛的誓约": "h9Mk",
}

# Optional user-facing PDF filename overrides. Key = build title, value = the
# pretty filename (with .pdf suffix) shown in the success banner, download
# button "Save as" default, and the markdown new-tab link text. Falls back to
# the on-disk filename when an entry isn't listed here.
PDF_FILE_NAMES: dict[str, str] = {
    "内波拉克斯": "内波拉克斯攻略.pdf",
    "等离子炙热之刃": "等离子火匕.pdf",
}

BUILD_CATEGORIES = {
    "武器所属流派索引": [
        ("剑盾", "weapon_school_index/sword_shield.png"),
        ("大剑", "weapon_school_index/greatsword.png"),
        ("匕首", "weapon_school_index/dagger.png"),
        ("弩", "weapon_school_index/crossbow.png"),
        ("武士刀", "weapon_school_index/katana.png"),
        ("长棍", "weapon_school_index/staff.png"),
    ],
    "通用连击神器分析": [
        ("无连击", "general_no_combo.png"),
        ("风之歌", "wind_song.png"),
        ("精密", "precision.png"),
        ("元素&诅咒&谈判&炼金", "element_curse_negotiation_alchemy.png"),
        ("神秘", "mystic.png"),
        ("学院", "academy.png"),
        ("通用增伤", "general_damage_boost.png"),
        ("通用生存&功能神器", "general_survival_utility.png"),
        ("所有消耗MP武器的MP补足方法", "mp_supply_methods_all_mp_weapons.png"),
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
    "单独武器/流派解析": [
        ("裁判官", "single_weapon/judicator.png"),
        ("内波拉克斯", "single_weapon/nepolax.pdf"),
        ("等离子炙热之刃", "single_weapon/plasma_blazing_blade.pdf"),
        ("图书馆幽灵封印研究会第2型", "single_weapon/library_ghost_seal_type2.jpg"),
        ("精灵融合杖伊洛妮卡", "single_weapon/elf_fusion_staff_elonieca.png"),
        ("书库之阳亚达玛的誓约", "single_weapon/library_sun_adama.docx"),
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
show_last_updated(ASSET_DIR)

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

    file_name = next(file_name for build_name, file_name in builds if build_name == build)
    file_path = ASSET_DIR / file_name

    st.subheader(build)
    if build in BUILD_AUTHORS:
        st.caption(f"✍️ 作者：@{BUILD_AUTHORS[build]}")

    if not file_path.exists():
        st.info("该条目的攻略文件还没录入，敬请期待。")
        st.stop()

    file_suffix = file_path.suffix.lower()
    if file_suffix in (".pdf", ".docx"):
        # NOTE: Browsers (esp. Edge / company-managed Chrome) often disable the
        # built-in PDF viewer plugin inside iframes / embedded panels, which
        # makes inline PDF preview a never-ending series of blank boxes. We
        # simply expose the static URL plus two large, obvious call-to-actions:
        #   1) Streamlit download_button → direct download with correct filename
        #   2) Markdown link → open /static/... in a brand new browser tab (the
        #      browser's PDF viewer works reliably when it owns the full tab).
        # .docx guides get the same download treatment (no in-browser preview).
        #
        # User-facing display name can be overridden per-entry via PDF_FILE_NAMES;
        # the on-disk /static/ path stays unchanged to avoid breaking sync_assets.
        display_name = PDF_FILE_NAMES.get(build, file_path.name)
        static_rel = Path(file_name)
        static_target = STATIC_ROOT / static_rel
        static_target.parent.mkdir(parents=True, exist_ok=True)
        if not static_target.exists() or static_target.stat().st_size != file_path.stat().st_size:
            shutil.copy2(file_path, static_target)
        file_rel_url = f"/static/{static_rel.as_posix()}"

        size_kb = file_path.stat().st_size / 1024
        size_str = f"{size_kb:,.0f} KB" if size_kb < 1024 else f"{size_kb / 1024:,.2f} MB"

        if file_suffix == ".pdf":
            doc_mime = "application/pdf"
            button_label = "⬇️ 下载 PDF（推荐）"
        else:
            doc_mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            button_label = "⬇️ 下载 Word 文档（推荐）"

        st.success(f"📎 攻略文件已就绪：**{display_name}**（{size_str}）")

        with open(file_path, "rb") as f:
            st.download_button(
                button_label,
                data=f.read(),
                file_name=display_name,
                mime=doc_mime,
                type="primary",
                use_container_width=True,
            )

        if file_suffix == ".pdf":
            st.caption("不想下载？在新标签页直接打开即可（会调用你浏览器默认的 PDF 阅读器）：")
            st.markdown(
                f"🔗 [{display_name}（新标签页打开）]({file_rel_url})",
                unsafe_allow_html=False,
            )
    else:
        show_wiki_image(file_path)
