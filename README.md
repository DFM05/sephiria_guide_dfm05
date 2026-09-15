# 赛菲莉娅 Sephiria 攻略站

B站 DFM05 独立制作的《赛菲莉娅（Sephiria）》游戏攻略资料站。

站内内容包括但不限于：

- 不同版本武器排行榜（含分期详细分析）
- 武器解析（六大武器全改造一图流）
- 流派解析（流派词条图解、武器所属流派索引、单独武器/流派解析）
- 游戏基础/机制解析
- 预设合集（六大武器可复制预设码）
- 网站更新公告
- 全站搜索（主页 / 侧边栏回车进入搜索页，搜索页边输入边筛选；支持中文 / 拼音 / 拼音首字母 / 模糊匹配，点击结果跳到文字位置并高亮，基于 Fuse.js + pypinyin）

## 运行

推荐直接使用 uv：

```powershell
uv run streamlit run sephiriadfm05.py
```

如果已经激活虚拟环境，也可以运行：

```powershell
streamlit run sephiriadfm05.py
```

## 同步攻略图片

站内图片素材由 `asset_manifest.json` 记录源文件路径和站内目标路径。

检查源图是否有更新：

```powershell
uv run python sync_assets.py --dry-run
```

同步所有已更新的源图：

```powershell
uv run python sync_assets.py
```

只检查或同步某个条目：

```powershell
uv run python sync_assets.py --only 物理剑盾
```
