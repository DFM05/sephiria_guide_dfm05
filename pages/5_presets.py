from pathlib import Path

import streamlit as st

from wiki_ui import render_preset_grid, show_last_updated


ROOT_DIR = Path(__file__).resolve().parents[1]
WEAPON_ICON_DIR = ROOT_DIR / "assets" / "wiki" / "presets" / "weapons"


SAMPLE_CODE = (
    "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzShC2uxTUR2hc6FOUeKktWD8ve"
    "9BEM5LTwk11gkYzEeOQtE6H50WxVUly589U7U6sG6uF+DZkp37LRnxj5ba"
    "ABZMUIb3KYilVWyyfNL9/LDr0\n"
    "+v+AMgFG2jkfuPIfLJR0nBndp13fJiCJLDZdzfGl5XzWekV2XhWO6Z4/EB9nq"
    "QdL82esfQrw3JlSw=="
)


_DEFAULT_AUTHOR = "DFM05"
_DEFAULT_VERSION = "1.0"


def _p(name, subtitle, icon_path, preset_code=SAMPLE_CODE, notes="", author=None):
    """预设卡片便捷构造器,保证 author / version 统一,排序按 icon 里的编号由调用方自己保证。"""
    return {
        "name": name,
        "subtitle": subtitle,
        "notes": notes,
        "preset_code": preset_code,
        "icon_path": icon_path,
        "author": author or _DEFAULT_AUTHOR,
        "version": _DEFAULT_VERSION,
    }


PRESET_DATA: dict[str, list[dict]] = {
    # 每一类下面按武器编号升序排列(按文件名里的 1001 / 1002 / ...)
    "剑盾": [
        _p(
            name="星光闪烁",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnh2vxXUA2ivKZPVHx2UND1SESsMHWRMopIpszBZwT3CFbmeD9UrAJId6IjZRwLNAW3syZFLulgLeF7Ay5Avp+eczWR6jALxH4u5dOwbCXtTtM"
                "AlL69GzDvWi9Bi8yNsXy7f/3kVHxM3vMeLQZTQTXTs47KOpAMF1MYK9oQqGvFkWcjSH1+8klsvYillSHufCRNPInGFYbBf6sU09MYAC8dFNo"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1001星光闪烁.png",
        ),
        _p(
            name="冰冷愤怒",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnC2rxXVzyhAjFi/ftx9STiPaRXT0gham2kFTUY1eTeQoTYSa6ruAlnikqZ0VKUlHHOt3Cnr5CRu2JfNY5VwxQPyTwCcJuw5dA9Vky/86gqNJEgVMkIlYjxhP+1n01CDR8w2fxISFExb6sfPj9GwQtb/xJ7wrM1M8wXKXGXDjPpZx294rvqgcLpHnSXg2JuekfeZEa9y4hWZsDpT9tX/ILEo1oYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1002冰冷愤怒.png",
        ),
        _p(
            name="岩石剑",
            subtitle="物理剑盾-非攻速/守护",
            notes="奇迹：猎人/侍卫；不推荐蜥蜴之外的服装，不推荐换掉天赋耐心10",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTid2qxTUA0ErIa1iPP//tfArfvbQqk/73f8KexzJ4T7iNbGSlO65yksetIBkVq12hHLoyZrDaY6dsUg6QmnLE43mriDjJGvfMTlRiK43G3z33VPs3MUuavZDVxcgH3W53eJX61pD08bPv/vvlUn2tx6Gvrmy0ZONGirErR+qhfXDhbK/0B3XlpdFwkInnTUZCF02Cq+cafmtN9wOI3+6lldFM="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1003岩石剑.png",
        ),
        _p(
            name="灰烬飘扬",
            subtitle="物理剑盾-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyyie2rxXUDyhE71CzFIBsyGX7FvgDml4xt6zdo5hbOTCY5IGCkKLF2EJknp0kcvhY/Bf/3r1dExRgka2ThtIoT2OItc0SA8jPAcA0VTgFgVn+OXhXsvQ3rhKlWNaoD67ajAZaMxPjJxfXQqU3+owNBFg836FE4XEhC6AiBjnRU3wNdJBJxB7yE+PBYOXJPWhLQlerI74hwylLUG5N6VvkFQg+yIjXmPKLQ5p2N0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1004灰烬飘扬.png",
            author="Eden_T",
        ),
        _p(
            name="无垠原野",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnC2rxXVzyhAjFi/ftx9STiPaRXT0gham2kFTUY1eTeQoTYSa6ruAlnikqZ0VKUlHHOt3Cnr5CRu2JfNY5VwxQPyTwCcJuw5dA9Vky/86gqNJEgVMkIlYjxhP+1n01CDR8w2fxISFExb6sfPj9GwQtb/xJ7wrM1M8wXKXGXDjPpZx294rvqgcLpHnSXg2JuekfeUknnsiFBV58Ejd0euKwgte2YXJl"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1005无垠原野.png",
        ),
        _p(
            name="收紧的恐惧",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzShh2uxTVzyhMiF72sgzbxTdvDDTEwiHSwUHQ/Zs5qSio1CtbWVRlJfOVrNyXY3hzGmupK+pgK1TkdjJBBJQoZmL/9LKBtj8YlpZilfiF9SrWNMVdwjKUPC+kP9F3u07NMfuA2XADGYjIpw9Ek85xELDdDYqGFcKT76PpoVp8dL8cMhSqhoDeFcF6Z5QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1006收紧的恐惧.png",
        ),
        _p(
            name="收紧的恐惧",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSgB2uwXUD3hA5FQxoIR79RhhEsDXbVv71EhAMkUOGbGVlzfIyOGU9Dnelh1Ch8/18Jm5TDP2TRQ7tnUbiRX/yH+ZG0yLmzGVu8Abx9rrToUCFEYeJFUM/mazzsVPUm0/hEPXLxvNUs0yPGnqFbKcAFuU0k9CQFnBqwUCCLLfvr8qgYOlwxHpritbf29g1kxohfbLmYmSbBeJPynFOpZXNl"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1006收紧的恐惧.png",
        ),
        _p(
            name="归来守护",
            subtitle="物理剑盾-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyih2vxXVzyhAjEG4EpMwfIujHNQqLNu1Wqouqo0ZqSatie3Zu9IjENNxvAtDjFHiqSplurkNqBhsc8TMwCwoHuLKAkp7HfQTt1KeI2nsfSgGk0S9zoxCNKnztJ7Oz3w8VSyorA9X1q2J8hXdiYHgdeolxhWiEWJViaJXhtns+RcZwUKpFM5i1UUQ2DhGN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1007归来守护.png",
        ),
        _p(
            name="胡萝卜剑",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人/决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnC2rxXVzyhAjFi/ftx9STiPaRXT0gham2kFTUY1eTeQoTYSa6ruAlnikqZ0VKUlHHOt3Cnr5CRu2JfNY5VwxQPyTwCcJuw5dA9Vky/86gqNJEgVMkIlYjxhP+1n01CDR8w2fxISFExb6sfPj9GwQtb/xJ7wrM1M8wXKXGXDjPpZx294rvqgcLpHnSXg2JuekfeZEa9y4hWZsDpT9tX/ILEo1oYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1008胡萝卜剑.png",
        ),
        _p(
            name="胡萝卜剑",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTgB2uwXUA3kvLcPVFbCNQMmTBIFOcuIsR69lucbb8Tp6X3jbaDnYMbox5sC/9toXWq/9w1RJ6L+NiBtY2jJuyR4XYeMEUTV7fuE9RFmlRrO8x9cjROB0AB339nDjHLD+XUb8IlQjH+7Gk1GHG6dwv/RP5+FeTPCdSQ86TMdPhLS8Se6E3an9Z6sS5Gn9k1FVLhKNfnyl5ps2BfxcfGvnNldA=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1008胡萝卜剑.png",
        ),
        _p(
            name="葱根剑",
            subtitle="火焰法师",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTh/W+wXVw3kjuc5xXavMYUmcztw3v0w2Pm8HvAtXmMueS/DjBLlAaJl+V1segWSQ7D9d6pdiAFD0cmEWxJxqqhWWs9FAIW6oopPQA7LZM19Fbv7X8swK7N/WttQl941XriZ1s1CtAsza3NXjnx32fcSX4+qFv/10BP48tWxp85yiEw4GrEtT7JdtMfCd1UAc1stPxchoWc5aa0jKfcUBCPg/gW9ZSKJt4PnIxbFrpet7OH2VpyMoR31OdYD21kdFM="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1009葱根剑.png",
        ),
        _p(
            name="葱根剑",
            subtitle="冰霜法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThfeqxXUD2HvKb/VbD1BBYF2y+Vm8NcchmaAMni9t4j55VVukyLYBUuJ2EhU4/5kvw9Ymmh4AYPgYcIwRi+d9UXzXscpBd2jVBKkJxnDevZNu05DlRiPye+MSsxkmZz1BsHnHJaK8u3ZTgTW0sDC80ZM/YANYfBSkowGD5EqAssrutvUSOYV0NfkMucNZl2Te8K/XlEM7Z5J+tBmXXuE0SN2zhnCPcgL6HMZ4mirsZghdRcDAXRMEnGuNvZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1009葱根剑.png",
        ),
        _p(
            name="葱根剑",
            subtitle="闪电法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTji2uwXUD2ivLZPVDT+sacunETlH2gy+0WLV+s9mYROb0nYiqLfVXWR3ePYMdfbLXTDIivlJ66q/ajdc+yRPlA48MDcRRW4Xpw6QFMuHEl4SXfPC2e/yxhSQHpaDc6c1S6+9y8H40AZdPXy63Jz0B2jd9r02mypXjvwWQuLeUmIN2i7gjgEt4B6AM8YAlBTTh/bcxpCDLHI1OKsA1qmT+XU1wB+qWY4g5OrZy8tYkL9tOVxIC885zDsr+WlXaUcYj/RXNlSw=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1009葱根剑.png",
        ),
        _p(
            name="葱根剑",
            subtitle="双发回旋镖",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzjiyt2XED2ivLZPVG1/I2pYqm3q8PfqoHsOfr4mEmUuGbZeJEx22fwmrmmeWk+uLew29pr1lFR7dedIdZ0KDNPWkFtdhQ6n0iRPQAt8JWH/1Qf5/LHVak9KGCp91jkL1r0MmHZiNDEyVx1eHVbC3f4iy/MTk8CdnHkUmniyQF/lO/1Vvvrs2tsAU/vmRkAAMVWjGckJXYQo7GPssh7j0S37iBX7MmQ8amOsZy9WOCtMxTsF31jTc+f0ZyZAA4bpv0HHln2q0Z4QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1009葱根剑.png",
        ),
        _p(
            name="闪光的细剑",
            subtitle="物理剑盾-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTih2vxXVz0ivbbPVglLMfIbLRA/cusZLa/e9NnW77z4wJ+G5i1IuFa0PkugR6Twdaj9uyTn1WEpI5FFeEBk+np4UjvIeiIpn5ZK5+XXokjrRsrUQRTaW5ox0lkEEbibGpz3yNsQIZxR7lgLy9c5f1VagxGsDdf+9K95bHYWZLm6/lrHynEkGDbAqtfXk2jwNZnaRFbGhx/wJ8+Vx7V33i4pKxTBh1wKdP2qGN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1010闪光的细剑.png",
        ),
        _p(
            name="闪光的细剑",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyi/WuwXUTyhE71QzqI/a72BUQU9BsdAHoJ6Lo4nZxrCbU3+t9NktdRVjT/ae6Ak1hmNq2SAQ67K/s3DfE+LuIkFS93BO4wEsLQveSlEnJo1cpkxUrybVar+pM4Tvvi7ID2ESMlNsbtruKrYU0cSVfSKfSvWaCvxUplM0lS8PM9UyKFg7XStYlEhcMBCfiKvYlDjOE69prVWe8NsPQb8oSmzaoFryyZaCwgRGJ0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1010闪光的细剑.png",
        ),
        _p(
            name="火焰凝视",
            subtitle="余烬",
            notes="奇迹：厨师",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbbPVghDB/IbIJTSYkwbvFVFbYcgZw1RALCpsf9+kwsp59ApGQkwVMPjrSlj9h6KqruUKAL4UDyvGZJzoBk040rqdfmlufa1E1WEcB+ww/5zGhoHUhGNUBOVeM1LJ2wHdvVS4VnJu25UNlOhHLEXzE7Sg+h+jumnc4yx1K6YFvz06MyG0uIpE7jKNRebpjQ4tctlouGiiEZdHhJOemXS2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1011火焰凝视.png",
        ),
        _p(
            name="火焰凝视",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhC2rxXVz0ivabZ1ghXsaz2A18gEwA2RzpS9XnkB76jm8R+tdVrOjB2kT8g2wlwUMNjrSlzdh6Gq7uUMAkCOB1wDwAM9ZmOuYT/gBi8GA+aj40QeVigAVvdLteBTxyblm015Z8brP22jJ0P+u0UlcbcXF2iwciGvYMdWwnpBBIJt5TXK8uS8SO0HESGbWsnTRRDlqRmFmody/FF3Cd4wnpry42us0nwWovqRryaG5uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1011火焰凝视.png",
        ),
        _p(
            name="冰之呼吸",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnh2vxXUA2ivKZPVExLD7pbDRSwMFmZvHNyI7cmbXDKddmJ19Jqej4HYhtSavJ68HKmpZ+5oet/zEmJzfHySK7DXJ9Aj85UmvR6COVaeBhUgs8LsuKJy8BoCH0RERJ/SVkqXlIJHPLIyUvj+84aGeCeVDhiwrAJo1Fim1X5sXedf4H3vqbYBbH79Jl/xA+1XKBLIlvosGV/6w/kGo9hsw4iIPRtL92Rbo0MYfLnm9uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1012冰之呼吸.png",
        ),
        _p(
            name="冰之呼吸",
            subtitle="白狼冲刺攻击",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTijWvxXUA3kvKZ/dLx3WEy6TN7BCZjMHji9T6By54jdbzmA16Vu79pnel9WLl0c44a/1yqTNDwZgkS2SRNUIT2OOcxDdTvhPQcg0LTi3QXn8OXhX1/3QV50UU4BXxYxcN8bSvGVQDywx81SrVlhIw3OVsMaRSnu8l3TwxSDQ3cOmjH1HjJw1dmoVyioxeZk1sA9JAwI5LcaZKGwrtEkxoqvx/jfn8tVRmPQWN0"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1012冰之呼吸.png",
        ),
        _p(
            name="雷电之翼",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyi/WuwXUTyhE71QzqI/a72BUQU9BsdAHoJ6Lo4nZxrCbU3+t9NktdRVjT/ae6Ak1hmNq2SAQ67K/s3DfE+LuIkFS93BO4wEsLQveSlEnJo1cpkxUrybVar+pM4Tvvi7ID2ESMlNsbtruKrYU0cSVfSKfSvWaCvxUplM0lS8PM9UyKFg7XStYlEhcMBCfiKvYlDjOE69prVWe8NsPQb8oSmzaoFryyZaCwgRGJ0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1013雷电之翼.png",
        ),
        _p(
            name="冰川之刃",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人（核心：驱邪剑鞘）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzi92+wTUD0EmG7cMFTZTNffrDjZ6VCvav3VyI14PIjqTxlcKiKG12S8+X1MfgeT0zDORwKm8TK/UKm2nUfsoqYAV43gjTMrgUUiSJvIzYKaHZJv9omkClt2WutPSNCYWLGYnHabXNbaXaumtYA5coXsjbgOutSbT+P/mxuemi1c3sEn2ggUDfOR1E3+KWnKMtKhF8Dx70SZCT4ihupaNTBxKox/rScvRI2qLd5ml8wOItiY2VaJmtzbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1014冰川之刃.png",
        ),
        _p(
            name="暴风雪的前奏",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人（核心：暴风雪之锤）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzhi2vxXUD2ivLZ/dK1+UZU1aETUCnhMYdX22Y3Ji4RvAfXvQ4U2qr6rfXx8cHiSKsjtruriHYTGfiUqLiAitsYeDxmBPgs3Nfz0UPn20y92bMUM0wJ/C1ZyyHc1EVhx3p5kFc95j9NI2QgdiYdccwcyz3/fHsxb7FBnwLSRBUZRznUMzutuJYxasS3QstlWh0YN2zWslmfqBMft/GBYKVanq5Qvo2Pr94P2eSFL0hxd7v1kGZtRmE="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1015暴风雪的前奏.png",
        ),
        _p(
            name="暴风雪的前奏",
            subtitle="无暴-冰霜武具（所有冰霜武具流派武器类似）",
            notes="奇迹：探险家/冰锻造师",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzii2uwXUD2ivLZPVHTCKCZv3GjFefezEIW7sdmjZpzmnRjQg8UQ8imkm/LdYVhGZEQee3jfQQUO7lz3S9zyQnGGEUGuejPud2IY6Tv2vO/xYPJK2foAGQESREKZlG6d1TwgL/WhhsATdkzKma5Kg9pllVAMeA9lTUpb4c2e+raaQftMHruxYM+kdTbeCZzRIZapJA1e+unEk+X17X7kcu5or6HnD8sumMFBlVqlm9uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1015暴风雪的前奏.png",
        ),
        _p(
            name="暴风雪的前奏",
            subtitle="冰霜武具-湖泊",
            notes="奇迹：探险家/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzih2+wTUA2ileZPRoeSHq3GDYikgvAyElTIq/NOoKl6RalFaCAE2sDc4keI1vzSzcNILqqgPYN+7He+nUfNooYIKIrwDRLvkcUSe1WYzgrj2Zp/1olcGptXXStVP1RFZ1S4BUqFBzrBqI0aHV1Ou3hKuUGa67zTwm17WwtgUiWsHM5sc2J9x2hOdbM7Ru5hMr2w8ddWZ3hQPDWedfSlYTdYGJ0rh9SvdS7p7/qE3Ut/aDe0lip+HqVnCqTmXSdbpOEfHNlSw=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1015暴风雪的前奏.png",
        ),
        _p(
            name="暴风雪的前奏",
            subtitle="无暴-冰霜武具-湖泊",
            notes="奇迹：探险家/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzii2+wTUD2ilfZPRoe1iJvdnTchzsLOyLSKoVqlZ9rIex1Qk+xVUguXUTeh+ys0Sin74iv8wQQhL5glIG6IXOVrhJcWKmgvdBBlc5J11VNJ0WGZH/uWe83eTGAVcHsPf+yMOtl2w08dGt0CmTOWwrJE/JslvghNrWfvHsGTzgbpUWMy6ah+zmzriYTxWUSufUDN5IyWcku6KAFimznJvYy0ynExin866KAPd6J9NTHLZgcu51rgQcRb0pzZXM="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1015暴风雪的前奏.png",
        ),
        _p(
            name="弩炮剑",
            subtitle="同伴乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZwShC2qwXVx0hQjEi/ftRY+9kfi/pwPcMvbmJvelzoGTefm+/igLHbC+0D4zMdk+TcjDfd8rJsJAeKyPsCfZgyUWEJAajolrQgW55OcVNskw6kJXOVtmEMY5xfn2Qih7YXIK42GGbfkogbWB7533PaP1zU8qhithbw4sTjvngV0z9nfx6+eC0rfYfr2VCO0e3IsAf/kfd4blzdNu16GA+ogTTSXPmKiaLchHbJAq0X9vQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1016弩炮剑.png",
        ),
        _p(
            name="超导体",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyi/W+wXVx3tU43ivf5jc72BTSjA6bXPGQMBysMKYOTQX0S7LWaQ/2I0GdKBuVt14ChfHwDp4kGILsD+D8M1jMa7gYKGnYE6QYO8Mq53aUgVnLgwH/CZPJK0U08BLH2YdRUwfBnZvl8XzUPGDXrYLPsa1JoIlZyzs9IksDyuReNDtGlm7fSxYVHhcMBCfiKvYlDnOE69prVWe8N1BmhS5ziB6DzWAlkFbqKHWN1aW8="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1017超导体.png",
        ),
        _p(
            name="索利斯使命",
            subtitle="太阳剑",
            notes="奇迹：猎人/陨铁铁匠",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWuxTUA3kvEa1mMLVKisAXf8wRpkYjY10y7eyJ4ji88GGmjlpoYbNZ1eY7xfwcqOkPZ7Dvae6CHZqCkc5sVcK5sApVoSkxkLAaUFIXdwgDm6f70sAIXtBI57ZmuxNB9gYNk+V+PVae5wvgnc2Z9sm1nBPDP/WBUvWIfbHxgTaaCm02yXegKTTuiXl37AaW9u"
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1018索利斯使命.png",
            author="Eden_T",
        ),
        _p(
            name="食火獬豸",
            subtitle="余烬",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTijWuwXUA3kvKZPVFbqNYcPzASxSEvIkTWT9hCKFaSeS8DTD68uXQ50jpO9ZD/C+9PbJSZ2NIxDkf/CRzZgOFFcJHgw5tPaX99PAJIX1IeoonRUUpqTWSoVeebTHDyfIho0UgtLROrzBfuRXw9Ey/9/e5Ury5nlOAPlNp6UQANcJwsRfQBrx/SP4Loyr+TSOD55wmU+m7rep7ceU/qnzECrlNoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "sword_shield" / "1019食火獬豸.png",
            author="Eden_T",
        ),
    ],
    "大剑": [
        _p(
            name="无视",
            subtitle="物理大剑-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziC2qwXVz0ivab50X61C/epVHPyOBNLsjmhht2TWky+pmdIH9saZeEfZpjyNh0ct4ARa0edtmbuRQXr32PpayriTGs0LkkP9NVK88PYMZ6amgvhepYKzWlr7jtpEdlZYZgOeUl8ul4+SstC+cqRcanIahkYU9EYXh21a0DWypfKRrN6ZvIJVYXnR0w5jf2l2IQ+zIqHnY0uAV+AI0/"
                "uAqdh+UHLp8V4p9tvWGVdHJfrm5pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2001无视.png",
        ),
        _p(
            name="爱的眼神",
            subtitle="物理大剑-非攻速",
            notes="奇迹：猎人（如果怕MP压力大，可以调成20智慧）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhfWqwXUDykjObPVAfLKBZcfDPI8Ki+zmq8CF5aXZ7udxlalf1nouLKUdVEwSQQ/nsfw+fmJYWxgf3gk6iQG6hwzR0L3OJxwPDUxDTK+FKLxQ+ogK/SgluN7Y1xAF+rPZjAds59vrpaVY9AvVT51dYaE0MAv3Iu7BAIdwl5J5f4Dg3vELh/Sc7m01j+/IzkhGObZYI0eWGALTtmfFc/"
                "tJcAyw21ofMpaPbzOhr4ioS5ZdpbWE="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2002爱的眼神.png",
        ),
        _p(
            name="黑铁戟",
            subtitle="物理大剑-非攻速",
            notes="奇迹：猎人（如果怕MP压力大，可以调成20智慧）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziC2qwXVz0ivab50X61C/epVHPyOBNLsjmhht2TWky+pmdIH9saZeEfZpjyNh0ct4ARa0edtmbuRQXr32PpayriTGs0LkkP9NVK88PYMZ6amgvhepYKzWlr7jtpEdlZYZgOeUl8ul4+SstC+cqRcanIahkYU9EYXh21a0DWypfV1voRPbLJ9bs+KMye8ZmnQCekotz99qstEYRBbscj72m6+QVGhjiALDeoXTCvESBr"
                "m5pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2003黑铁戟.png",
        ),
        _p(
            name="短暂自责",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyziC2rxXVz0ivab50Xy16hqBMcKOTLFcgwpqppTtZ2TagBlQl89l1VEAW5pBv1twdZfN4y7n1L0pI5FKOEBk7ccX4tuwYYD4zKhOJg15YUu9rijqzbp6qBgPT9/lqF0bIpbZ1PZNUsjBFulYyDZ4SP3y0+"
                "d3SO4Z8zGBmH+nPFEL2HqB4a3kU4COBmNAviyiOWT0siyEA/zbrIOBKqm6rDMvYpnBj8wio55QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2004短暂自责.png",
        ),
        _p(
            name="短暂自责",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWuwXUA3kvKZPVFbCNQcPzA1VMKiu2irLCOUbZ4Tp2U2HSNKOZ0Mr0LNuVDnX8Lhz4BZrHMxzwRq+5WdSicpp/CxOxYIAlea+UFj5asleMRk1UYOAnV9d2Zpjske3AoTYCOlb0GZJyzvetc4Uvf1b/"
                "5HBORz0obKXhlERPZKSpjxau+WBclrItt21hyZk4G4TCWy+o1vn+2wJIxyZXM="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2004短暂自责.png",
        ),
        _p(
            name="红蛇碎击",
            subtitle="余烬",
            notes="奇迹：厨师/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTh/W/xXVw3kjuc5xfaIj4n0032y8L0CYfyS/7TO5wTk/eozBM862wyGslt1MhCT8ijdV8rLvSxGwNgcp/o1qgwaTcPQxyWdfS1Ar5Aiov4eVEEWWvtUfPpYDwIvqvSrtJjJfPpXDaJBFIAY2hvQdFYVH1NU+UzQKh37OgtCEymeQMZ2Rh+3tM/R2/H67buk7TLHteQlo6PkgyBGTUvs814wyL2ny/ORKiKGBGOaW9u"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2005红蛇碎击.png",
        ),
        _p(
            name="红蛇碎击",
            subtitle="红蛇之眼直伤",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZ0zih2uwXUA2ivKZPVDTiLTDosyvaWbZzHpSBjqZR59TqOnlqry8KUUYS+BdtrYBhvWP7pQXQXAFl6peFDM/xMI6sxl7h7nm6r12Aqth8W587I/BIQKrhT84FuQsc3rSbISnadNLj1MA5Xcjj70LhP1xZrtkzULDVZ1g5iA8qcpLLJbMH1JQm/U4OZlGnyKh0Qmj05wA9nYxoAJMiLmgeiaqP02uFE4qk5qEqluZv5waAYViiCs3F3FzbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2005红蛇碎击.png",
            author="Eden_T",
        ),
        _p(
            name="索利斯西涅里斯",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWvxXUA3kvKZPVFbGOpR5aE+UDlhNNcgEM+yv57LdbM3hLYCVwCK0PlO9RAoQzet6BjKn1XR5DZ7U71tZxp/fNwEvEj4A2ucdxFLdwl3fTZOQ+nOUcwI/cDXblVzdRjC6941HNIPn3Ygmx7PCVOo2dPe1V3ngy+lb2KX6NEG4zUopqvl9R6CJDe1KPmv0zCUMM6sws6Rlk2RHXWfC6bYKYUZD4x7GRl51SjLbG5vQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2006索利斯·西涅里斯.png",
        ),
        _p(
            name="索利斯西涅里斯",
            subtitle="太阳剑-陨铁护肩回收",
            notes="奇迹：陨铁铁匠/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzgjWvxXUA3kvKZPVFbUENU5aE+UDlh2h/z4yzeyJ4jIT3nA14Ve4RTudE6DWMkwVN37pSlj+B6aIy684HflXGyBcvvsIrlJ7xJhaCkJaQoJcPUnmVPWWhwtyvNt6EyLzGrL/ZghJ01wWURxUhpTUR+VzfEHcw8a4vmx7Uyxn6YzvmPH+XDK/hQZQ6mzwroTlWSu1gnMPvLXYgCAk4Pv5XQj0jMmXA9OmQMvWN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2006索利斯·西涅里斯.png",
        ),
        _p(
            name="荆棘棒",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzznB2vxXUA3kvK5UNKkReHpOkCjV1Rez8oaKMN3zRkT3CGbz9sL2byV7jVqSJx0x3EUXewXEiT/Y9UcChtqKxAv2aOkD9UYpU3DbAOUZENShFoTSEdezWuwrTRmdvlwpTDpBC78KtJdx9JZY35pVABdz4d62/R9uDRSxt3WhfL0ClegaICdVwVqTpA255qgn8ZxxlHWmiL7gIAg1185vL+dlVNoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2007荆棘棒.png",
        ),
        _p(
            name="顽皮的恶作剧",
            subtitle="物理大剑-非攻速",
            notes="奇迹：猎人（金叶非常重要，省着花，也尽量留多点到boss）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzijWvxXUA3kvKZPVHxRejiYLRzLzlFxKrL8NRE2Z9T2+CgKGf1VgD8Mw5noatYyYfVyL6H3NLhJ1dRJnAMHdTH9pxEYhrYrTYwE+Rf306BlI6C2B+4oMYab/W7QlXCLNAE73NtG0OuMytvey9oaUukyUemfQkq2SPHbHFyDiza6GHbP3haPJBohaPh79TF9N6V0g9VWByGaYZNIqVGqEeRdbAU9EGM"
                "S2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2008顽皮的恶作剧.png",
        ),
        _p(
            name="吱嘎的脊椎",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzne27wXUAyklWYUz66Ct2RyOz5WXVUyV7gVQ9cPJ8T+ltKVaSXuC46Id6ouF/nqcn3rJDB1OAUeFbyTqHaLKU/Sxwzx0TeeBgiM/UHTtrDXHx/DkLLj2c5Mwb8R2dzt/l+RQsmRMuvI/I0YUZmbXos8qIddyh929WYxLHYaXAAszcsK5I7OBSerfk0MN0ozokgmvHlvsiCoA+akqykkL5ZgLS0HHLNjUgurmN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2009吱嘎的脊椎.png",
        ),
        _p(
            name="吱嘎的脊椎",
            subtitle="风之歌守护",
            notes="奇迹：猎人/侍卫",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTne2rxXUAykjObPVEfmEJ/7MXUJerWfYjIF4Y5Z7OTCU6izE2clK14Y5Hs/d97yta3xoCNU4G1PaOQnIcAtzspFiNJL9spV9459B4lyqFUrlm3vLooMhjPGoZoBMx4pYBGZ+bmdne8+9Iogi/ZR0tcbizHbUszNs2KKpM0RTjf1R4m9xutOJ1ANVpA2p5uOtDiKH6xk4kcTxJtLnLvgyBy42vO3kcCVPfR1H2FaW9u"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2009吱嘎的脊椎.png",
        ),
        _p(
            name="万年寒霜巨剑",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUQ2kmSXU1qMR0WDqi/NV1Resz3UdTje6LeT4WjmL0cBXbBVIWZK4iklgsV3rJDB1OAUeHalbBA3U7BUTxVdrZo4jHYuwA7U6T6UD+zxKPTAlxz9IwRIBZNu+MVr/ZMR9vU0avw/gelF2QccJVmpIWKt+E1hccQ9LBz/JGBhChxkx0I65TYKpjuKDfMgNFkeLv6QkJS/UaSVWhaVdXYSfHqBS2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2010万年寒霜巨剑.png",
        ),
        _p(
            name="万年寒霜巨剑",
            subtitle="物理冰双元素配平",
            notes="奇迹：猎人（注意要物理和冰属性要配平！一般建议只拿元素词条神器作为属性）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3kvKZPVHxXb6m3g1VwzbdbLioq9i5l54YRDzG5mnuHvQ+IUA403Z137HYPN2CnjbBZksabblb75S8/h7sDtRrmoT82YagTQvKxh3Y/dtW9PjoHVNvS9UVTf26Zfc2fPYbTWpNaleLgsP1WLZyZD25Ieu+djIIUVA+8UfktyQsqF+hdTuaMcwOb4rBbrO5oYIcB/wc3L6UC2+bHhlW/149Q495QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2010万年寒霜巨剑.png",
        ),
        _p(
            name="冰柱剑",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi92vxXUD0kjO7sBNGRz/p2M1s4MuciXMjRbm7xC6zfcDmQ0+tmAwXPQYloauPChcvupYI7gjygtj0Qq96KZavhbDQbTQpNnRQ5fk0QfA7zWpYzVIcN6myuwdM20PS7H5i8fL2bXsTYNpVQyYa73LUwdcL0SUgQAQ7HYUGo4CaXejZusdEanCFUZkVoqYDNiYY/KWwgdorE5af4aG9sw0N4iKAMdXc5p7cXuQLjoNtPZOU2WttRmE="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2011冰柱剑.png",
        ),
        _p(
            name="驱魔的重剑",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人（核心：驱邪剑鞘）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzih2uxTUA2ivEa1rNyzKT5Cf/tAQr2QJsC4+81Ji6RvI+Uv04Ek/6ueGWlZe5YSE23m5OoVob7IjT/kKy1Wr3IN8MO8xquMclq+oZcYMwyi9r06t0IjxQl7nDM2iKD91R7qWrgqucqs9I1Rzw+pWPb/8dcJSFrR8REAJdKNXrC87vGjPCHratxx7XT96GiZ2huXAn+TdCevmgVXAwdKEgRJROVwkzruIYWDtIf7hZ2rnqQb5ZUTh95bFBy"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2012驱魔的重剑.png",
        ),
        _p(
            name="深红漩涡",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3knCc51daqLZZF+yvoyUxMiX5h4TfvZuTcuAghTJ8gq2EIobgbRxkbuZD9ayjn1GEpA5ZaqUBEyXp5UTPRdQSlcRw5ICgwQvMel5ibwL0G6U4V/T9SqgBOQYUBfG2fckaTUoPYlaLgkc3Ct1XRw1JwwUF/kgPV5TmfUcklCSsAXiWrl9MNu2RJgEznqIqEi9WCMbI9uvTmth8CFNJwnS/r2V5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2013深红漩涡.png",
        ),
        _p(
            name="裁判官",
            subtitle="无所属流派",
            notes="奇迹：猎人（搭配不固定，可以按照教程举一反三）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZxT8DWqwXUD2ivKZ51uxXT721QciAJMlsyyf6U6BsJ7jdaT5aluP/T4DE8S8W/gzAHTSFDTijoST2QCelorBkz3Gt7OwU3Wt9CvqBDglqO0soG9reY/9hdyYKWVeaH0J8FRS1T/z1NGnOhPxe68KBwXvDjvOy/jJtGaq9bZghpjufLaBYNpF4H9ZZu2fW+oHAOaFWDniIS84/wBmQF4dVOUF6D7L6B+jxHR3LrDj5BMZkwQ+HVP5N3vIrizK+f7RiyeFC0355QOKYpSzE3WIpFycxdWWRki4vvn3ZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2014裁判官.png",
        ),
        _p(
            name="电击大剑E3G",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyh/2+wXVx0hU43qvf5jVarnsyTQHYzwnmqzeSj5aWXSVmyb9NNmPoIzfku9ZD3W8HREpQItcr20u289zRrwzAZCFnvb5JvvioPCaPdl/NRBKQv72VqpnaG9MFf2nFeznMRVvIiwNRkU1QSdCoXWav9cUuksWh5JFBKHTFr1TLTxDcB0Tv6o53gecKOAErSHcdYvMfE2p1TCAyvoq0CmbgoQb6CnAILNdZtbtg33DRnQG5p"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2015电击大剑【E3G】.png",
        ),
        _p(
            name="电击大剑【S3G】",
            subtitle="魔法科技",
            notes="奇迹：电击术士",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi/WuxXVw3EvCaUFUjH7YT7YVFq8I94TRc1vodQZWTwatfcOpueC7dNj7TYRU+S6wgTaCfkI9CRkVmwG8YRF3QvVbeFZ1D8f7FU0mnNbpEJmDBKTpOqvSJ3eFg8s5yBgly0SmvJDraDhROG9fhYONFbejybC8+RXozRrXR6upSG3T/Fsyb/d8EADbupgrQlbPgqLyuvt6qrfsJ95uooue2SMa2evwUlduVQWN0"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2016电击大剑【S3G】.png",
        ),
        _p(
            name="幻术师的遗产",
            subtitle="火焰法师",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThd2+wXVw3kjvcPXCxD6hdKk/c4W00PGmqmeQ9AW0cOQBlXODOnUiTB4BkCb9Qaj2q56CXkBU1MicQjxpERz3sy4kL7/j+h59mg+CWedYe686tojVmRGz6L0toVplajfoyb9MljV560Cw0YN1pfGokKE3OkwVFGCIqDDQ7O8/lO9bPXCAwyOs9MAm00R812eZklSW/gfOv6X9FBvUIDrWxaeS1Sb+6kNG071iql8UPrbSXv/4j/JNzw+16EGxkdFM="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2017幻术师的遗产.png",
        ),
        _p(
            name="幻术师的遗产",
            subtitle="冰霜法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTjDQqxLVz2inieO+9ICEW7DCvyomU3dqlX1XIE18fbWrONImW7xIeXRd9ceyaOh7MFV0Uf7x2Q/7MWwdj48MfdhdkuPqSocZrTuqjzV4DE9B4/SCYBjOWvD4301GHYVTR3WfphxF2KIM+bynsx3ERVqWzmXN6FbnPW5KRyjk7OokdugqfiKfBi7wm0HSFTHaNu4qDzPhCQqoGRPqk82i+vjeZmssrNtsKTESyXsprx2/kY9U+/gVoQ0iOckN9GdVNo"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2017幻术师的遗产.png",
        ),
        _p(
            name="幻术师的遗产",
            subtitle="闪电法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThjWuwXUA3kvKZPVBb8sYc82/MK3QeOC4y9/aLo+SSea9a7z588uqevCoozLxsCs5P7AyDrjzFIkQK1RtnJqtKI5Yj+b4x0jNIr9epGBX4W84idZzQA2ZNDeRCEClsaZhFOoDIDfB55bhnaaZD92vkpHkmX9j4deLrQz0y2AQ3y7T/L9sVzRbGLSBYK1ZQPn5C424MPsoJdJlbqNWLyxoQPIjUjz048ISCzq8ZNxm1ivFzYzy3WZqPI9JdJGN41nZpYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2017幻术师的遗产.png",
        ),
        _p(
            name="幻术师的遗产",
            subtitle="双发回旋镖",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzjiyt2XED2ivLZPVG1/I2pYqm3q8PfqoHsOfr4mEmUuGbZeJEx22f42rmmeWk+uLfg7fqPmISdgvQiohXnp0enHkODVAKTwe35rlfi/26WrhjHj2c5aODA52PmJRJe6ET+PzrNkUwMJAfk0+RpkMEUXWh8PGYwACFMFEEy/xZHoQAn/vNnKxVBY8whI4ilzMaMdUldTDyc0yKFEjNUzawtH52VVZyzoFem4p075xZy171CuYIUHhEfijUsSpiW5+nWYKMgcURdQGN0"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2017幻术师的遗产.png",
        ),
        _p(
            name="太初形态",
            subtitle="物理大剑-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3knCc51daqLZZF+yvoyUxMiX5h4TfvZuTcuAghTJ8gq2EIobgbRxkbuZD9ayjn1GEpA5ZaqUBEyXp5UTPRdQSlcRw5ICgwQvMel5ibwL0G6U4V/T9SqgBOQYUBfG2fckaTUoPYlaLgkc3Ct1XRw1JwwUF/kgPV5TmfUcklCSsAXiWrl9MNu2RJgEznqIqEi9WCMbI9uvTmth8CFNJwnS/r2V5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2018太初形态.png",
        ),
        _p(
            name="太初形态",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTgB2uwXUA3kvK5UNLxCNQMmTBIFOcuIsR69lucbb8Tp2U2HaMKGZUoox7AtGh0/1+99YwbxPmWszJ6VdeXdfEH8ZH0yLnzQlcGURVpGXjcs71UXTtOx0BxSW5pbsku3IoSYCNFb2Gjp/8zGHH6d3v2fz7GFOR/0qYBd8uX3gYBOR2STW4MnLsfVbYLXCyLs2CT5HEGsDHeSf/uaW+uZXNl"
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2018太初形态.png",
        ),
        _p(
            name="拉扎里恩",
            subtitle="同伴",
            notes="奇迹：将军/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZwThjWuwXUByivKZPVHTGEbq1S/UabtzPJ8CLGXrjaTnOY7cFUDOaTATEwA9YjgUhW0rlRooj7KNv3RGvhUXDBC+HQnvSLMM9Ca6DwQkBHT7D0LZoBbVHZM850yJ4DF6TEDQBMNAJNv+gOAnWOX4RYh8bEw+J29xUZmAP0/OSlNIAD+Bw3ut8e+XLjF/iyf2IUmrZwWVk0Sp3ubDxKe1GKxMWCzVj6nEoZvEeFcZuvLEQokGyUspMm9zbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "greatsword" / "2019拉扎里恩.png",
        ),
    ],
    "匕首": [
        _p(
            name="无光之刃",
            subtitle="物理匕首-攻速",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2/wXVz0ijiTUmABZmFNbGcTN3oQun/gU1cRnCG8odZHq5Qx2g8Mj+QlUtIzaDyp68aSnzVwmh00uxnxoZrUOHLf6/flHEPi4yM/Sn6f1CIv6e/Jd6Wsm2dfRuCGcUtIovqqxnjde1pSXQ8eHT4FmA6XnL9n0ijBZMSBSCbhpIlC11w1i7GMFOIBKR6GFP+2WhnRXaKgRmFy"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3001无光之刃.png",
        ),
        _p(
            name="无光之刃",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2uwXVz0ivbbPVghu9wOPH8Py1OTsfuPNBhX7Y4TdnxQFamKLY1aHYh5xCpHynH+2dWZRKpyHrA8abeFq3g6Nscz4qYBOXjqykMCR7lDB2cw7I9T4shrW9UtZxhajX1rPt83HFNiGfSrOh22+Dn+WFUrkerrkMF4bwuOW8oQDf6H4wD0DoVMdh2D0s2bR7IeKhWfiF3Iv1vukwT4ahPB5ZGOYXJl"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3001无光之刃.png",
        ),
        _p(
            name="绝对向往",
            subtitle="物理匕首-攻速",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSiC2rxXVzyhAjEi/ftx9STiPaRXT0gham2kFTUY1eTeQoSYSa6rjBF5On24cE+m+/KZxe7vplQ24uJQWfsK7T69hzq2TcymIFHSDuIgHClKxQIRfMbQPrcb/W/0k0yQhApIPL5dhrN4TBMQYg1V3s3G/MjQOs/+HDKtBhyae2hY3q6V52OcV2y8thy6R3MnCx1ho+VoghScxyeqtG8W9dFuk23YXJl"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3002绝对向往.png",
        ),
        _p(
            name="绝对向往",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTih2uwXVwyivabPVght9wOPX8Py1OTsfuPNBgX7Z4TdmRj0Wxs6lfBn3W8Cxdn5mvlt57ZvK3BoQVrioySygXvojCRMxYub9EHURXp+RAdxXN4KyxrI4bLLGs8xuO4ePt/M3NgpoMTCMy0IQdIKcBVAX4juE7YqI4cHe0Y1PynqbiISvTvte2RCBqQhjhD4cCJcEO+nJXLHBxyFJTmSa9ldFM="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3002绝对向往.png",
        ),
        _p(
            name="爬行的绝望",
            subtitle="物理匕首-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThB2rxXVz3ivaZ5136C6V/BMdkSa09tP9zZmKPsJ6j1FB0VrSRrpCkH8nhoV6JWymyigiv9pbf77VnCwdcYUeGvEL0RfsrVRUNBLtgH/XZabb6/2UqxAg34d27NLFF78nK0c3rBsYdOWE81oiBAbwixJk3Qf0Q078eMfaGSgM8CEyS4wJUbJv5jQ5KvYQUt2NLTMi6bWFs"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3003爬行的绝望.png",
        ),
        _p(
            name="艰难实验",
            subtitle="物理匕首-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThB2vxLVw3kvK5EFmhiQZR5SGioyURzyrU7T7BFo4j1TN4MLSDl4pBGWhbo1D7W18gH7iKJeAbnBjtQWkLJ2vnDtojNArmbsTdAm2si+/bdVhOR+di12tcY6Cml7d4DMag4FWNoJ07op6JJkp+v70ZpVETxUqQFyqRG7LtobmmaAr9MqYNeYlZxvKGWYJ5Qt6SkrxpbWE="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3004艰难实验.png",
        ),
        _p(
            name="炙热之刃",
            subtitle="余烬",
            notes="奇迹：厨师/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTih2uwXVz0ivbbPVghtt44PP/KQgKesWuh1AOJOB0TCiF2YqmAlOB6piZ7CwcqRdGTkpMIBBIXKttNEZlxBEB5fMyH4M9Ib78e7MOxT85+o6nkeS1eSb9gtbEpwA5+V/xqZHet3O8MA9NTE2Sx3AdQL0t49PT7Wm+2LskfFehS2m72sTwhykuAuES2R7ird5xXHgC0pV+h/15fyruXusafdLgJaqiJS2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3005炙热之刃.png",
        ),
        _p(
            name="炙热之刃",
            subtitle="等离子",
            notes="奇迹：赌徒/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzT8DQq2XVz2inWaZ0hEql1c7FE0XuTxTAaHeFpQGLgyvJ7bS4Axao1JvfBxkUo7gv/2X+BBOjDRz7WYnhzbIIwupn7/W85hOm0hT8wUkZk/uvWQoUMV9IjAPkEazMc6LVkyNKd2YUMtIqcxCfFtcGEcYsWoAThhVOtcy80Z3DppR7NttngNwXSNa4N/3MUFuXZLmU1ECylIp2CEdKaHyXf3R+QxEp+srsSQUHS3yfGWzqmHpBAshIFjNYSg/9Yqm5hSioKK9em27gyHnZ3R3UFmnuPpGWJnMI0WZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3005炙热之刃.png",
            author="小林家今天の饭",
        ),
        _p(
            name="索利斯·因贝尔",
            subtitle="太阳剑",
            notes="奇迹：猎人/陨铁铁匠",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWvxXUA3kvKZ/dLxXUaj3g19gHQugVUrxAAikv6iDnbX9pO7qe7+zg046wm1ayBq+4SfAb01y0OJrv88Ysay7gZEXNi3dfSy3D3cyLj74vBaSVfxYHpsrApqX7tALg1yZnqjxrZxe5L88CVoNe35Y9uISq1iLlgB7x17W4Mi8H/BbkndIJNSGdQk/irF7wrjDNGcniXnGe4xcbMGznSXGvuv2a+C/pgCCZJ1UZ5mmmlobWE="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3006索利斯·因贝尔.png",
        ),
        _p(
            name="索利斯·因贝尔",
            subtitle="太阳剑-陨铁护肩回收",
            notes="奇迹：猎人/陨铁铁匠",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzgC2rxXVwyivabZ1ghDMezGLRzwzycqRzpS9XnkB76PnvJUQ7hg/bV1EfTtlIgqN6uug+mLuWjor01PUfHhuAkSwnRt3ryTs8j5Pemy8Dqj0DgDOmOde1lIPTNaODz6YzCcGqDtGAT4szF/gn34ZpWjurPpYwky8DCXil3d+UsuFqvoz8fK/iwZA4Vu87rTjWSO3KLdcYrXqnJTNwDvpTQiSggkHfHMCbqvGN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3006索利斯·因贝尔.png",
        ),
        _p(
            name="笼罩的阴云",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyij2uwXUDyhAhFG4GorRYIMW8k9dvA3eUJ6LrKjZpz2sll0CyOvOC3/AE0Q/NxPonnzthgGhveW9M7PTl+bwKjxEDcxe8Srn3sqh9M7o1bw9Vx6xzi5uIOL8+swwFqR0mx9fRpRmlHHfQZHSZXisPBcLFilyRYKzJ8EgR0lEwN1/pvy2Q/2KxqAlS8ArmAztmws5JR2BRTsaKDwstGiJmYBD0WOvhy064PQGV1aW8="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3007笼罩的阴云.png",
        ),
        _p(
            name="雷电之怒",
            subtitle="魔法科技",
            notes="奇迹：电击术士",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi+2uwXUDykjO7UNLTqg1f3r0TRtbA49w6q0aRk+J7A7GX1r8M3MV4JdkjR+LHr5uA+ShFDmDFdEUs4OgkHeYsqih3iPBSGnI0Dzn36apxKXc2YeMmVAIB/iNmFuDuF/7j1B/67gQAwegG6xb1CTH4sEXsZztJgpAv3c3NasoYioA3OCr020CpiJS5zB7PdCEzmJMCVC4fgZAVP9plGEG/Rb5oYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3008雷电之怒.png",
        ),
        _p(
            name="福寿草",
            subtitle="物理匕首-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSih2vxXVzyhAjEG4Eq8kQIxkKoLBsl2HQNBomdbOeDiTtq7k2AlmJt0DpO8ZCrI8EROF/6hEIro4a/ULNfLuqZz83FMzS/Y77Zu2JytO8d5FtH8X962eZMNIFGQ3k+ZLQqMpdwLDAiq/zXy81RC1LFOgcEEzo+FGE4P8QRYI9RTBUro4i0XGaxdCmK6I4nVmG3thCBv1kwuLYgEVBJKSkiqFNoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3009福寿草.png",
        ),
        _p(
            name="黑幕",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhC2rxXVz0ivabZ1ghXsaz2A18gEwA2RzpS9XnkB76jm8R+tdVrOjB2kT8g2xRA7T9r5pO85v4I2WR3UZ4j0iCzcU/q9kRtPoejiGLK9KZKcZ/YSr/YBakTSI3IMl5DXCzPcVZN1C0EmVNyavIOOGSZKxtAlcEhI9+KsfTR0k6Atuwcta3KbcTNvYbTKhu8hGFpudv0n/rfqebO1+WuCPqBeinCokyA5R4o6qbjG1vQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3010黑幕.png",
        ),
        _p(
            name="黑幕",
            subtitle="同伴",
            notes="奇迹：将军/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZxTijW/wXUA3kj6fU2fxeJrm+Setxeak6eYFATbQX5uTiNFAXD48KwmKGQi/aMffDmfU2xsJVjDhFMVYa2an1PJBnirFwwPV7frMqEouEMW0LFtbM/JNQ9dlrBoqZuAqZEkQS1uveJrrYWscihV7jtBoKU+vn93b3fdhvkvQTTczzmfu+PNCZLoItY5IW3IN1X21VjR0TwYvCqLbBJfEikuYgvXXxcievlpk7F0X9iu7Xm9pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3010黑幕.png",
        ),
        _p(
            name="黑幕",
            subtitle="物理匕首-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSiC2rxXVzyhAjFi/ftx9STiPaRXT0gham2kFTUY1eTeQoTYSa6rjBF5On28bOoYKzZsL6H3NLhJ1dxae7U6+safsHQdhfuKetNJ9M58sckjC377C6JEHSqPDv51eWWVXpRFkPA1P/6AlMABbuQZbdOol32fR9MRqwZo7NSn6w8jnYb+0ukXy7LOB6eGZ5EpMjITpNRSb6W52yRHa5R5nxu2R5GvnJlSw=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3010黑幕.png",
        ),
        _p(
            name="无尽沉浸",
            subtitle="物理匕首-非攻速/影子",
            notes="奇迹：猎人/盗贼",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziC2qwXVz0ivab50X6H6rLcKg0MHRpxF1SL8BuQmtOvpYfKWwKrbD249fMCHSBJ2lzeQi3kx4RnIxdorZLIUhKyH9BgzZPwTcB0zc8MjULiwtBcQhuTQmy7QHRBhHcrXswVEfwNLbo4Xe/28h9K2N2DNl2GyWq4zujn3H+3eVfMHpgQfHItshFul4s0h5aGXkte/ALGk+FCefKBKumeoUa6iUlFmoMoGg9mv98nW9uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3011无尽沉浸.png",
        ),
        _p(
            name="模仿之书",
            subtitle="火焰法师",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThd2+wXVw3kjvcPXCxD6hdKk/c4W00PGmqmeQ9AW0cOQBlXODOnUiTB4BkCb9QWj2q56CXkBU1MicQjxpERz3sy4kL7/j+h59mg+CWedYe686tTut+S2pP6DVkZpEjrQXzcTPkhkhMA8/HHRVYO3HU6ysu5Lkxh+fg0svgwW5d2DkwJbXYM0HUvb3jYJr2CXx76fnFtETrGVwcuxqHs//MTz3TMOja/AziHBTIlDqtmduUyF7zMoRxD50qvWxkdFM="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3012模仿之书.png",
        ),
        _p(
            name="模仿之书",
            subtitle="冰霜法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTjDQqxLVz2inieO+9ICEW7DCvyomU3dqlX1XIE18fbWrONImW7xIeXRd8ueyaOh7MFV0If7x2Q/7MWwdj48MfdhdkuPqSocZrTuqjzV4DE9B4/SCYBjCUI59APDGPaj8BnlVd3tGngZoefTB9ZNP3waWAOrO7ZYrm8zndx4SuCe6BJvLp98HZqA7zj+Oc6gfdvB/NcyoOUn6C1yqLvG8rxhzh1xwM0sCqs4P2y3oRRdEGKXTzKyRbekFLuMDCzV1JoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3012模仿之书.png",
        ),
        _p(
            name="模仿之书",
            subtitle="闪电法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThjWuwXUA3kvKZPVBb8sYcP3ATlE2gy+3WLV+s8GqROf1jaY1uS0CS5aDgOy93yjMkm79rpvg45jrPHZJ6hvUb993R3evcuJIoPTg8rYV7dDnZeu2ZVCxJbEoY9yOATRDMnOkKuVTlQSZzW3yv8Cb0Bdkus97kqXlQaoFwx/VYF06zqBGEAld+fk5zEMhF0OXOzGz9IMw6jx1Ft9/g/SWiwJjzgK4SENuGib+RPNDVv8eYtRavL1meSKh01/qVVHZpYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3012模仿之书.png",
        ),
        _p(
            name="模仿之书",
            subtitle="双发回旋镖",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzjiyt2XED2ivLZPVG1/I2pYqm3q8PfqoHsOfr4mEmUuGbZeJEx22fwmrmmeWk+uLf87fqPmISdgvQiohXnp0enHkODVAKTwe35rlfi/26WrhjHj7f3Cx8lOHU8WvoRRPQSHVakv2yg65hnemZY4ye1QWFKu37b22DtDuByJEqndbxsXdFSSe/068EbyM4z/snkkvK56RWRjMCJ0mFhsRzBQbQWewWOPvyWoJznCnHppJpjmFlyUD2pFMmlromZ0A634n6QWkF4QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3012模仿之书.png",
        ),
        _p(
            name="学院魔法剑-解放",
            subtitle="坚固湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZ1ziC2qwXVz0ivab50X6H6rQcOgUozMAHeUWNQBqLJGOgx4d77LTKuzZPXM9tNFxrAE5y1mRELVSXoEVcKaXDetTrCUDE3Yrd3/LF+FuMUlZqXuWe/LZsqO2yTlLQhH4jVlTdXmmVBB/dOhlRwEhi295ykLG9QK2q+st32QSHba7tQhTamUcC+35eTUDpKg8Zj6fqCO7lbr4ZMaTFZq/IBKc423fFEURzFiA77nCliDkTi/ZYM9vR2Fy"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3013学院魔法剑-解放.png",
        ),
        _p(
            name="学院魔法剑-解放",
            subtitle="太阳剑湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTjC2qwXVz0ivab50X6H6rQcOhAEP8aHejzdrMpfd0Ut77pzVhsl5eo71yyy5g0wVRg0cE6ENaAXpk+84eVsPUQJWDfqx2lHdMdt5yPyftySVny0SmJrByYekgaT2DuTygwbfenRBvJ6ngoS2NLbRry7754FTQ/8qfqB/93DeCVLNKS2Pvp8AToqh7vxm7J1SAgWEbUnwTIBjWO/j2gnU5BMR3T10hQiL2c7KGGxocdEnHvLhZKmze1i8fWHXB+KDbie3NlSw=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3013学院魔法剑-解放.png",
        ),
        _p(
            name="学院魔法剑-解放",
            subtitle="冰川湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyTjh2uwXVz0ivbbPVgh+qjQcOhANEtOg66d52BtrOp7mb92KF+Pn+AZVfcBZ6aP33gRlIUG1ANwtjlwyoiakovqDMy7SvNJtG8x2yLRGGCo5/uSLa4xjo/FuEtPRng0DZS6ze/lZwEKKb8gW8W5Mq6FbZUkYWSYQWc9+lVMsxKy73R11Cu0FJAEQ/fBqn+rWQtcT4QJL/yUZ3vLBMlfG0QNIaEStsYYHGmvvlfgx4LhvA+mFLYA/b7VuEsE7ddUalJoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3013学院魔法剑-解放.png",
        ),
        _p(
            name="学院魔法剑-解放",
            subtitle="魔法科技湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyTjB2qwXVz3ivab50X618MOPH8KqzMAveyJDHNh73ZDuBpheW2Gjjg6KhvzBzLIBbz4Fw5avqSIMBH8HPsCCcz8dJZLnXZhf2MnVy4n/zZ8kMXsj3umHqEduwv5V0Fqa2EQAScrtFkrU5pHQzWZRf15rmaaVPk3+dWM4QRTDZNxbZfosHZ6qU7304a0xn/46vVilOdmz/DzatK3AgzZ96Te0r7TA8Kb4MQNLByYZhS4+giykE/BmOrpiDhmZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3013学院魔法剑-解放.png",
        ),
        _p(
            name="学院魔法剑-解放",
            subtitle="元素湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyyjh+twXFx0hQjEG4Eqs1S2IoJNKfRhDrIPVVJSh+FMPrj5Aj+wr8HiCh6QKFIYdMdMhnG08zr37/mmqpxV24eLmzO/27MM1YtoGPIAvRHYpYRi+6BHbvdRM64Q8IfRTVBL5HYP8YdAKLsnUHEQ0MexL7X+AS9MR/tqn+Mje9TasByvPvAgcXNxRj1TJS4tTu1yc3gbbFsamgQL5R59PmTqmxoDxyDisTAOxh0EsZLBhsfHW5qhsS+YzI+k2rz/Y2NAgs5CSmV5"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3013学院魔法剑-解放.png",
        ),
        _p(
            name="冷冻公鱼",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTiB2uxTUA3kvFSJSPkNxEzaigy4de1Od1YWG2w+88WvFv3P+rqUqyaFOMFJpIJRT8Il+YNFspph9pFlvLfb9kH2HYL8RqmWB7uLAghbhA3yXpojXpXems5o2g8GHI4bwNlNXQ7fYOGYlqqweHIRPXOo3vuZxV5PUgp0FvADX1Xqqp9+IPCkLBTPnx5AJxJb5ZTiDdliiq3SxxmvawgEvw2K6Vwmhz9zb6MfhCCb5r+X6ppbGFs"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3014冷冻公鱼.png",
        ),
        _p(
            name="德里法",
            subtitle="冰霜武具",
            notes="奇迹：猎人（核心：暴风雪之锤）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyziB2qxTVz3ivGaMHLZW99Y3gtkxNJiUre3F2XS4/yarQa4DWuKmS0H6jqzaEveMGDlNJ2KEagJSx8wc06iIA6luLia9/8+vgEPvdYuQsGzcMb4f5z0eYVU79Ruh0jgL/iZRyc2lBviNHogf7BV0KaGrX8724IoDWQs9QWF6/FmBvtNsb7JVBX2nCc4IucdBVbmw7hWF+izSVh5kywb3pJxcGVXi7FdlJuXaP/OCHGoauMVbVZjmUJ5bFBy"
            ),
            icon_path=WEAPON_ICON_DIR / "dagger" / "3015德里法.png",
        ),
    ],
    "弩": [
        _p(
            name="加速核心",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzni2vxXUB0ingc51faEBEbd+yvoyax3ftwzLsCzJSRL2PX6k4E/RwEnikqZ0XqGVcRPZQIBIDNGGBvrEIC7UOoKfSaYaoHYz3hMFoy5Q0u8rAXCL/Ll3bnv8vgIin8zmJAZmBvvgUaTdapg1rkTda6D3Yi39b7+IfWNIhivjKiH/K6/JKEopdf/BL3lCzSkLua4HHuUt6ZBXq0jMzJaiNrHaGJYXJl"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4001重型弩：加速核心.png",
        ),
        _p(
            name="加速核心",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWvxXUA3kvKZ/dLxXUaj3g19gHQugVUrxAAikv6iDnbX9pO7qc72zg046wklS0zjkV4rLvywEwJocpfoZFh3c+TArCrwemu9jw+vVolvXTZOA3krx45c7m0B38Bc7dF2BqqXeF6YrS/FQ1++p2rucul5xxyzv7xJni0xOGLiq6PNeVnX8PiIsSjzdE8fBZXD3kkzkRtwpHnVNm3iEjBYsr5Wzp+6CO92llyQwWxvQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4001重型弩：加速核心.png",
        ),
        _p(
            name="加速核心",
            subtitle="行星",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzih2vxLVw2inieU31MEAWwvkETyjMgPYc37PATR4yTcfDkL3/9rFdW0HsStZh/WyXScy/brpzQKFvvuaLWgIW/343u1G0TRzRcep0NBAyOek3fP0hg4+V5/+X91OFn70MKpELDeMgtKWRgNyJwSQf4xEdQzy9VGuF7rv1ao0KDEg7VZRL2aOKyJzC4ocRAXrAI7Oi5Muva2LmP5PFc/sKMrmwVDKgPp7/Kpb2BbY3ETG9pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4001重型弩：加速核心.png",
        ),
        _p(
            name="加速核心",
            subtitle="行星余烬",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyTih2/wXUA2ij6fU2eBTx8MgGzIZ0f+bSNSQqyg/rCTMfYa1eycqQfC2flmxcoimz/ze71Kxpgd0Azhs4gViLDbBCkqAO87oUsYNbyHoRQMai/HfUg0RfXoKyc9Vl1ABfI44xZdsrURY0Apg2W4UW9EAWJljA7wHjG8HN/HdcbkNrgMlAEDOCBwaZjEykU3NGlokXPb4zCt6d8mkmfWjRAS2okcQgV6sTFOAhAZACH5AoSePutD796XPnRzZXM="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4001重型弩：加速核心.png",
        ),
        _p(
            name="加速核心",
            subtitle="固伤",
            notes="奇迹：赌徒",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZwzijWuwLVw3knCWU04gszuC/k8vBPMuxY/Q9xDpkt6cyEHKHcGxrFZEnajhzMsCbdcf1uQZEjZdpgm5I6nHnX878YfnOSm/oZqqxeOy3navTxZZXCNPQT9DDY39N2VWXYCIDynk2PbymKhPx5AaUHWw80bN5HxzQHD5XMCwdZMFJgW6jQElW67Xrf+W5hLsRox/uBH0o5zU+Zz6WD9PZqXXjFNoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4001重型弩：加速核心.png",
        ),
        _p(
            name="双子",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzznh2vxXUA2ivKZPVGx2aNB1SESsMEWM8spIpszBZwT/EjX6k6EVECu3/l5WelYY6AgrLizGhRztBwZe12s8Au2IBb+K9GoArr+edcTsm8PbBXIRvPbpXjsbQQZRESi69A85aUtXAdqccAqhmAdC0bQpMsBL6dZSzSnn4kjBQVoBDkicxPl0rQus//lDF0oxzwdUj6Xr1nxrE8GLq/lgt0KtoP38oVjvsyJYpN0aW8="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4002弩：双子.png",
        ),
        _p(
            name="赏金猎人",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnB2rwLUD3inCWO2XwOK+xlvYRxHThtC1UZxeBvyDAmb5+KYATW82SagC/QlEp1expWzyrtqQdOsOidw6furli/xdKry9x8vrca0OrYKavCNdxQDf+pAQS6M111yN1Spa8zOZt15zlxJLpQPBl8kfwv4CWuup5EFszJBpHcS5AozC20T2ApNXLJLap3p0f7WBB90zeo2FsRg=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4003赏金猎人.png",
        ),
        _p(
            name="火药合成",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3knCc51daUENqHMfM+TJFRL3L8NRE2Z9T2w14MJyTuepeAW5J4lfF32njkd6qkogCl/0oYemX4NWsKIK7bp7vN6tdRNMZ8sSircLrQuzgP8OMRfymZiKfVHpZVuM1nD9NpjCvx9lKuDlOQ3T94g1ZaKz56m1F+PczwbfFedGSMyPuinmbrF3DZuG7DsiQv5XdWWaAyE+oXX2ySzaYZOI3qeucQWN0"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4004重型弩：火药合成.png",
        ),
        _p(
            name="爆炸装置",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3kvKZPVFbUENqHMdoRQgxRMol9NRE2Z9Tiw14MJyTubi5xk/40gklS6vTkd+qkojC1/3aREGC3bMI+vss2KdLT/c3tydP1AqRdxicjq030ti/Z2VrQiQ6fOVlzV91RHK7BculR+U53Cryr/9Xj+jJ6OOuTjKKGdhbFCViPfxCrEt+iFGmh5lV2ZencajD8LsH2V0EnEKJ3J+bD53WRzVgX4J5QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4005重型弩：爆炸装置.png",
        ),
        _p(
            name="爆炸装置",
            subtitle="双换弹流畅开局",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTijWvxXUA3kvKZPVHxXb6m3g19gDml/73L8NRE2Z9T2zFaGWH1VuTcRAZdY1fSSycpE+SCkLWwBtN1+a1tJjrXu0s9XwrL6YnRPiCHmXJS+baak94+kwy+N2euz23r7HsaqjM/5VJgxMFwR/FpWFpHAQ8idymgdVVf46CDIdpgZTosZytW9CpK9MNhP1/xkB3z21XPUnjLHhYBGk6iBmwqBes8nA0rgmLR5BW4mG9uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4005重型弩：爆炸装置.png",
        ),
        _p(
            name="藤壶",
            subtitle="守护",
            notes="奇迹：侍卫/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3kvKZPVFbGOri4MXU+TL9fbjbF4bLecWTCUaiKOvqpspWBwDy8cFAaWUeDC+zmhqy9hI0uqb39VgYAL2/iFvERhJywlh8C+S9LL6BYziJzIiFIZxmQuMBaf94raNh9ZkpYKBLE1cUC89wA+9se0YqPDjmLqr5mFQG+T60fFbddsRrf+3teQjXrQDz8nL+EwmLN4l2u29IgCC2u65Q8QXy375HvEgTds3H1YGVbWFs"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4006藤壶.png",
        ),
        _p(
            name="连发装置",
            subtitle="物理弩-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTijWuwXUA3kvKZPVFbCKBZ8U8UhCHZTDqqJPFJZQ+wvpY8W9LppupeAzOiEzKrJWR4ecg2tbmNqpfgvl1TmP3/bPYvAkoNfeOnM92/gbz41L2OtAT9LOUwVVq8+9RwrPl2V6c71OH44fYpbK58J2N9QFwKKSJbqrh88lF3IABKxNOVQHK9id1fg7Eu9YdY754czJs0DZD/Z1cnVuaV+8+M7gC7PriLdIKVSvyQWjyFQW5p"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4007重型弩：连发装置.png",
        ),
        _p(
            name="配备制导模块",
            subtitle="湖泊",
            notes="奇迹：猎人/钓鱼人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZ1zjiwuxXUD2inHY/VbTSt9IgEKuFEOgIOJ9qTdMZJU2vJ8G231Pjaja7VKlkrS79nBfsw1d7uChurzX0dp4OC59d8p0r1dEQR7JvJt0JVzOH4riIQ5X2V0c7WNFRSIddVxR9bblZUlIALVYPfmY0eJ4BedokmebVUMm5BTNuk8DCrNELgdM104tD0ggDMHMmwc/czTpVGVTmiuY6XafEWmU7GIRli5ntMAA9vTOvzxTHoncjsjy2Iv8170HXC3r2zScio43tO4OnqVlYIZSQG5p"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4008重型弩：配备制导模块.png",
        ),
        _p(
            name="迷你加农炮",
            subtitle="余烬",
            notes="奇迹：厨师",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbbPVghDB/IbIJTSYkwbvFVFbYcgZw1RALCpsf9+kwsp59ApGR0C+9PN6yjuInZVQWt6lytIcZT7YFEXtiWdfS2IrrAyLj74vb6X9I5Sa9ZpbFoxMxmd3x6e2stXH8PDcwxE2UJzlCzj3M10QznO3jEbWfFhJtHD4+734poiPJxACmaZE5gl4n+h1q09uAQGDOpwq0fnwRMSnGDhpuRS2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4009迷你加农炮.png",
        ),
        _p(
            name="索利斯·尤巴尔",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhDWrxLVz2inieOw8gl9OOMXckAJPxfxWw4yzGyJ7zYLMxhLURV+osnikpSJxkSsERA5QIdCIUCt9sEbl/zIVmFYC4QxQwTrM82oVMPNUiMTedwTZ6WOy+YTMEjW3HW1w5TfPkcCDlGPRjkxZuae+62J2yocCI6MDw8JUTZGahNeZp0GAM1DOEfDfI+50+2OkLzCPWmJIozT5v6mi0jCVq0OjJf5ET1LKPLvOWao5YGO1kbGFs"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4010索利斯·尤巴尔.png",
        ),
        _p(
            name="索利斯·尤巴尔",
            subtitle="太阳剑-陨铁护肩回收",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWvxXUA3kvKZ/dLxXUaj3g19gHQuGfLMA9nMki4LGvQcYzcUFxyPDhJBl/JlGVHYOt67TxLKmWxXgGQpNGtOBTXh1ln4BPqrmuZec0lByxfgReVigAVvdLteBcx/rkJ4BVOkqDD2wHO78n6NWf4XmvOO7Y/qyJNJni0xOGLifxuwciY/sDVwkDhchHniXFmTl6F6cB9RSBD+vvNsrcjEarDerhmefC2IRGABmWlmQG5p"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4010索利斯·尤巴尔.png",
        ),
        _p(
            name="标记稳定化",
            subtitle="魔法科技",
            notes="奇迹：电击术士/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi+2uwXUDykjO7UNLTqg1f3r0TRtbA49w6q0aRk+J7A7GX1r8M3MV4JdkjJ3JMAYvmzthgGpneG907ufnk8hSaGNwltU0dl0WqhMRBYh8nAsBkKw8q6w4q9nU+xmuWuSP/6RaeoO8qYqd5SPgaBfEWpTl/dcdrFO5znAWPUIAmHuzyFpmLtecEVet+L4+vhB+Ei4A2phj2fe9N/gLOZZiNNa6GYXJl"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4011重型弩：标记稳定化.png",
        ),
        _p(
            name="聚云者",
            subtitle="乌云",
            notes="奇迹：气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzyij2uwXUDyhAhFG4GorRYIMW8k9dvA3eUJ6LrKjZpz2sll0CyOPPVB0ULN2TZnYo+hfHwDQImGIVsTyMHcYjO0zwNTOTJcm+c1aeW+GS+oBGeTY2shWKHtMeBnh1EmX9ZTamoBAG2QTQszCEuy4dZt12O4C18vPnE4I2cL46+lIfa6o/kfhHtM7R0x2p2gvzSwXsnfg4YSfp8H/vYv2GyruTwjkHA71gakQGJ0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4012重型弩：聚云者.png",
        ),
        _p(
            name="迷你机枪",
            subtitle="魔法科技",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThC2qwXVz0ivab50X6lQG44qk3RrhoGo83Z51BlZ5jIIkzYikKu4PjkG/JdaXhSzdN6B5Jdj0y0+mk9+zOgOs6NtcsogtmmdBfD1c5pA5cBKgTSEfqCVWxvTdmb6F8CUi53jyRfl6Eh2qNV36IqkotLD8ppITjavD/UubWnIvlBz22KMmGs+8izpDpzr4m87zR19BlCD0eiZ+h+7J/x+OOoLJoYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4013迷你机枪.png",
        ),
        _p(
            name="迷你机枪",
            subtitle="行星",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziCWqwXVy3ivYb50X6zZvfpVGFQuGcOa7d2oWg/ombcXhhrBMM2c/Z8Cc17qQ5eGch8qnjnpyb2cJQinUNWkr4E8iciTDhljxlvA4BYewzbVv4vwMLULdIudRM1yNmb3vQBx32VGdmSNInOTH6A7hewf0eRISYYXhM9UurSMKdn295wxrCEHZI6TYO3F5aHjSRfACkRJaXqNHL5athwr4PA411bo0fQj2KQB8o5/1gQG5p"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4013迷你机枪.png",
        ),
        _p(
            name="迷你机枪",
            subtitle="行星余烬",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyTiB27wXVz3ijiTO+UMTJl9qOHxyOpWaHyhwR6bCZWTnXP/6i0Zujg6LwZ1CQcuq/kvNNnK9sCp47v5DxGf2gDCviJVjvA+mQuICXGEURR0ai/HP2hwRVyJPfGLyulww2ggJfFFrOegIfNKR0UBx2R15g6ARbwPD4VQ0AxbMwpg8rdIUMcgO/wnr77CpW7h+DAPkftpK7UR9JGvPYqtf96foM7C18vXsUqD5116riSlNB23WJyTkYtxXywvJ1RkdFM="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4013迷你机枪.png",
        ),
        _p(
            name="速冻结晶",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人（哪个冰霜武具来了就先当核心）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzi+2uxXVz2EvC6UFWh1Bmi1ieDAsNAqEYKNwxu3/ciO5s4NIqXke5raTnyYNf9SWcxkOUdkss5zwf32tZ4JRG5Dx2APNZQYzZiz7iCRy/u1RA17gqnEzKAsdhmhwpkT2RHbJxRZDpsc7GzelzdlVFpZbQNxGlpUwLXQfd5wTWAQQ2K3/Zw49tR1w9v5XkOknN6rwfsSseRRUgQ1Y3p08ghLqyAe4mUslL+OQrP2IRxPZxsD0OslG9zbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4014重型弩：速冻结晶.png",
        ),
        _p(
            name="扩展装置",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThd2rxXUD3kjObPVHR+UZUBccvxcHW6hxaUDIiyp+WmBRbcL6R2MiSzOn24MFIyzfldALPt57319aGuurfc9mR3XaIQZD8xmdxL5s2GTee2TFybpYm3bPYg/1so1RzeMhgJEiV/iN7wQfkO+95VdJ8ItleSb4drT3N7gAamu3kYJZJLZyxff614de7F0Z6aVWgm07oUwHl9USG4upr3zYlgQCzUcSOf5NRpsYf7xr2hxGktGbVAH3OY1FyZQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4015重型弩：扩展装置.png",
        ),
        _p(
            name="卡里姆的形象",
            subtitle="同伴",
            notes="奇迹：将军/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZxTih2/wXVz0ijiTUn8BWkTTOietxeA0uatdYfJVdBwTHYOzqSiLlx6Yi/U9tNEznOF5G7admxVSruU/inVQitJXAvaXgz+LFWYLxaMdDA7ZlMxMpDVz+CZXLklmAEHzNdR+tHmX7HJ9QTLjhnxZDqzyGPScQ0UWe0Xec/0G8MNCLF3V5ZNtzIjxLGEcVUMjkZsTc5awMesBUQnHJmxpN0x5nrW0FV8q9NiXDx6hl5XxzTgG32GT7k5zbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4016卡里姆的形象.png",
        ),
        _p(
            name="紫甲蜂弩",
            subtitle="物理弩-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUQ2kmSXU1qMp2mWO0Ajynhhuj3UdTje6LeT4WjmL0cBXUBVAW5J4ukiYnxN/xjK35i/bWnqjXDbE3AfTwIG5x/Uf+SsSeZOHNHSmIrFWYe8lnbnv8vgIin8zmJAZmBvvgUaTdapg/43xzkT2mNIDjKgJxIx/3W2uUjGO5OSsDOegAD4kF6+q0SnFQWUkeEqnzpT8gBuo69B5nyeLqJ4gHJlSw=="
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4017紫甲蜂弩.png",
        ),
        _p(
            name="XRA-9",
            subtitle="物理弩-非攻速",
            notes="奇迹：猎人（如果怕MP压力大，可以调成20智慧）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTiDWqwXUD2ivKZ51cekhr/vzEThOH7+0WM8GFi74GpzZ6ssNuSBEwD84oJisgiYstwQMccO9FB+rma/qYFPN3XdUL+zsBgTF7YL6hIZY3QxcMX4QQan7AOUird4xqReBJ64WF98hJD29q1U67ZyWq0Ke0b7WTse+Gt2Eb38yPM8dEqOkrA2ctP3spbTDH4F7JKjBcqcDOIcv1dFCMhPY4h64jOesi22hHCLmyZmDOBvhNA02Nty8KNbVBy"
            ),
            icon_path=WEAPON_ICON_DIR / "crossbow" / "4018XRA-9.png",
        ),
    ],
    "武士刀": [
        _p(
            name="名刀村正",
            subtitle="物理武士刀-攻速",
            notes="奇迹：决斗家/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnC2rxXVzyhAjEi/ftxdSTiPaRXT0gham2kFTUY1eTeQoTYSa6ruAlnikqrxz7S10SPZQIBIDNGGCn7yawECTGpBijLMGgWo56wibLF7TXJ8SzqzaJUPp/ZafIHvTh6bR2T3Bc7AE4N1vVS62wdv7wMwg3j0gmLyDJw88ud5TGFKUf/YxPrxR6ZbLA/GjYF9ebAnWvjJ2jL19HELi1RMwYdD2gNMaAS2V5"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5001名刀【池子村正】.png",
        ),
        _p(
            name="名刀村正",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnh2uwXVy0lAjFG4Eq88eOkfj/3EG4UFkLOfP0YoGXWS0zaX8NGw9BKWT540c/D2D+2ZWJxA/nboEDK4qguG0ewZsapyUAt0jJCloCQZcPzeeqAq3oCioN7keaHiPgp0an/1mhZoqgWKs56AXzYw/3DwPn5WQ7WZVRKOrqSFqU3a+LBymgmzFav/IH/Rb3EVLhKNfnyl5GvmE6isbYuHNldA=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5001名刀【池子村正】.png",
        ),
        _p(
            name="怪刀毫羽",
            subtitle="物理武士刀-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnj2vxXUT3hA5FG8Go3AgGTTLbXL/cTUK85E19Z7wYldYdb/WiqLyi9QA9YgBTcWeZ7RUKMqChhrUmnh0TN3duIWuXYONhrDQhShtcULWrK9gvO5bY6evaziKk0iGiV5YWTCItIjPOQHcGOS9TRYV0QAY9EMY9/4AANkUmBBR0wP4l+LHEEGDabKvFSvTfBgFsinGv2woumfxQai/avqOTqexRmnLqHn0Aq2N0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5002怪刀-毫羽.png",
        ),
        _p(
            name="炽焰赫尔巴努斯",
            subtitle="余烬",
            notes="奇迹：厨师",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbb/dbMx8Sz2BZsR4kwblQZ6d6CtZrfQqcS+n9tWgz3ws45yglBS8jDmVwrEvixG8N4chXsia8ybTtaXkEc85AEQJaviiOZOcb7YbF5Sa9jtbFqQLR3N3xre3etXBpaUC1wE2cxDlFTj/M2kQTnOTkELODGlJtLf4+7H5domPIzACmaaE5ol4n+h1q0t+ARGDMFNH+ljKzQjlMVavHtv2V5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5003炽焰荷尔巴努苏.png",
        ),
        _p(
            name="炽焰赫尔巴努斯",
            subtitle="无暴-霜灼",
            notes="奇迹：厨师（注意尽量控制冰属性大于火属性）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzih2uwXVz0ivbbPVghu9wIPf+iVSIVJauVrRJpsp4MRBuDn7WVhjytRH8ArPFGy1BaDpiK34mo7vJT7/mQuM2WDjqSjmX/015JdB5o4MlkWEIT7j8mYGfAZQMZDnl2dERabSL40o9RbXK/WOJQyCix8+rNYobCL+qelqVs0vcIKGuBxmZDrqWm9++FjLARcaARKNLG2jiHWSja5auWZXNl"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5003炽焰荷尔巴努苏.png",
        ),
        _p(
            name="海蒂",
            subtitle="余烬",
            notes="奇迹：厨师/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbb/dbMx8Sz2BZsR4kwblQZ6d6CtZrfQqcS+n9tWgz3ws45yglBS8jDmVwrEvixG8N4chXsia8ybTtaXkEc85AEQJaviiOZOcb7YbF5Sa9jtbFqQLR3N3xre3etXBpaUC1wE2cxDlFTj/M2kQTnOTkELODGlJtLf4+7H5domPIzACmaaE5ol4n+h1q0t+ARGDMFNH+ljKzQjlMVavHtv2V5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5004海蒂.png",
        ),
        _p(
            name="索利斯·叶克里",
            subtitle="太阳剑",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziCWrxXVy3inbaPVghLMez2J0eSfj+VBeAEQ++3I6j1NC5G6mDl4E7PIBE+dtIWyXfm1NI9yj1H/fjbI4YBPjubF+kNQEBplLPuM8qzubkgRIRYWcL6H/VeNEu7HnMvTg5dVNGUwKEhFL7sCULj+qGe/5osKdM/dc8EWOWXwsvVYtYK9iK/ZTSnNXVPFiyGPEW8OM6eoaFtEr1BiOZhkXKqYz4yEWeuZ3cvWN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5005索利斯·叶克里.png",
        ),
        _p(
            name="剑斩刀：飞柳",
            subtitle="物理武士刀-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTijWvxXUA3kvKZ/dLxBUZD5aF+SbX+MyX5KxsyBZwTfMDXvZ2TubgV7W+HMPjObGVQSzxL97SFaYgq57BPKMpUt4Qw7iDx7g7RGCvxPazzqAkD06A8lXAoqnDu8+1mbyRyIldy1eV44X4mivdxTCM0gQ1YzRdpwGhd08OFeTm6OXOXeew+G/e6sokafUyxiaiHc/peAx4+87Tbh/bOAJzi3juuh66Y8HEWfVSdApduQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5006剑斩刀：飞柳.png",
        ),
        _p(
            name="剑斩刀：破舞",
            subtitle="物理武士刀-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUQ2kvKZPVGfp2mWO0Ajynhhuj3UdTje6LeT4WjmL0cBXUBVAW5JBkUqS/lM/xjK35i/bWkOrEIC7UOoCfSaQaoH4z3hMFgy5Q0u8rAXiMOdSahhacpe1EDLaQt4MXVXRPLIDRtOS1eL5/DVv7ZCJv1OzMG+BDZcaGFHqylKhSiKDYSEOfii+qOeTtgQKa1R8Z4Z3C4/cqoDrcRq7ygW0ZdlS2U="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5007剑斩刀：破舞.png",
        ),
        _p(
            name="剑斩刀：破舞",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTgB2uwXUA3kvLcPVBbCKBBmDBIFOcuIsR69lucbb8Tp2U2HaMKWY0pox5sCxfuQ4+5KLyryXkQOLlx2S+DiQnGGEkHuZnJuRWAY5cpGqv3DYsJLHciwHawRWkhA6cRbFkYPj8/+QtI7O72rWfRyKbE5Pqv1yZhR9DKqdlfC0oLahmDkSX3sjGPBJ/Y/peXxHSqlp3x+4oUvDIicu+F3ciHdFNo"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5007剑斩刀：破舞.png",
        ),
        _p(
            name="优衣的短匕首",
            subtitle="火焰法师",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTh/W+wXVw3kjuc5xXavMYUmcztw3v0w2Pm8HvAtXmMueS/DjBLlAaJl+V1segWuWWvNQoP0lDwl/I785l2DGHlyjkE+5GHkm/b4sqB96mV2AkfX2ZPxWzoJEB5RGkOeSAnRXY11K9u6CraGk7BUV59OS5M4bwCQRQvACsnJAbt8i3A3nsbOdv8Ex4VjPMIKL8qRIRMBrelpyb94JOdOBijoLw/nFqolL4PrNmrNpHEIILSsAgbeom4ZlDyI7pFdVNo"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5008优衣的短匕首.png",
        ),
        _p(
            name="优衣的短匕首",
            subtitle="冰霜法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThDWqwXUD2ivKZ51Ue1sMcM2/MC6IzwGifmQzjWm6WuVBR7yiLfRUCEgByOdku/yEj9BIDFlMxG/MK852hkyVUIoMeyfeguCqe57D3uFcCqsalA3T33cXx0WEp92x3nZRjpZaFIpYDXxplFLBdRbd0A0TqKuUv5PWrRgJ9s7doYcrXVrGJYEwNfiEiSM53qRfJlEhzk0/DSx7tBmW0uE3QCWR+mtU30FOkoJnT794Fuh0WV8OaQBQ4Ik5WZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5008优衣的短匕首.png",
        ),
        _p(
            name="优衣的短匕首",
            subtitle="闪电法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi+2+wXVz2kjsc5xXa/MaconHsQ370Y/9+IkU73FCsvWppewhM+F2Cz7dUwyTyr2XNq7GSlxfQ9VTMX+T38WHUIYMeebaguDZmZ5A3gVd+VsulA/J+/cF5b2g05+pn/1dz15QOgslnezPNZ0VL7YD8aVYCwIqoWxOqpgBzegBfMOKOxbV+g25Oks0gEOsu5KY7RQN9zQ0G8yt00hOq14mbNPgLu5eoO4vCbJhLWxgXlIHHEgtQsLwCd14JXA9mOH53QVRkS2U="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5008优衣的短匕首.png",
        ),
        _p(
            name="优衣的短匕首",
            subtitle="双发回旋镖",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzjiyt2XED2ivLZPVG1/I2pYqm3q8PfqoHsOfr4mEmUuGbZeJEx22fwmrmmeWk+uLda0FYHVhETPzYahPgCd73WFz5QW1WryoVfk8uB2xOYvB4bv3NVEkfnxOtuzAIBQdVmadxBDKpvOCM4awNZBfdccarvBXEru1dMVkhiTRnRf5FcVRY4ZtdWWfEtbdKBgb06MPR69/FCvqvTlu9DdqcK0GaPH2gSoBDgroKL+gxwxoudZ5RUWHcutinrsrifiPc1vh45FDFcQGN0"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5008优衣的短匕首.png",
        ),
        _p(
            name="亚达玛的誓约",
            subtitle="湖泊",
            notes="奇迹：猎人（不要抓MP偷取，只抓MP再生神器）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTgjWuwXUA3kvKZPVBbqMYcP3ATSqYjuOrWLQXSeLWTgXh3rJ27WED276DoOy93Sg2s5Y2KMfHBJxIAGC/kjQ37e2OjcX5gw8lQL+HU+v9IjR3Rssc71n7pZ2VgSmP0mtyy7+YAMDf9ZczxkmLYMYOQ8hzC133/EQYJwH8WNuHkuRTGYQcybPtvQBBt4dce3CZouDbFi5XBkYvm6wOpkZSbDLMtD4DDljqGk00bsrDNlHX+w8v/T2BybQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5009亚达玛的誓约.png",
            author="h9Mk",
        ),
        _p(
            name="亚达玛的誓约",
            subtitle="书库之阳",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzih2/wXUA2ij6fU2WB13nRrjHYZUXWbWGoYk43ILWTyTKRpJu5ib8Rw2JmRbdA+7MrdcIPVdi5+ve2Py3tLjp/nvZkO88HE7yirrnHx0ouMwgBjrRCBHkh/rr9IGwmCBZ3XQvBlQIBYSVl1RfjFJoxFwlDFe+pi9NFRipqxBISCYVJ4kmuZvWlcMYS3vJP2bXOqTnAzNFokcVqrmDUg0N4unRsvEOTIt/lhnU3BQ31u0U9h5YFuurXlVAbPhAtZ1JoYQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5009亚达玛的誓约.png",
            author="h9Mk",
        ),
        _p(
            name="图书馆幽灵封印研究会第2型",
            subtitle="物理武士刀-非攻速",
            notes="奇迹：猎人/情报官",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZ1zih2vxXVz0ivbbPVgh+9jObML3SC0xdN3N4+00mp/r4w2e/d9dQUwsJV/AtGB9C85L3TybNMRH8Y1E6BTfvYt8plfdEz5lWDUs5fx2q8Iv1uP0AX+8Ff446Xmej0ELBHn3bSpEs4L6aetfy+1BsQGc1AvR8CLCTNFNjtyDlBk4K+MZI1bj3tYzKP2fujtJZYkRWKjTAcfKqaWZ2+6nuC/RBbIyNY93GHrXM2cnh29uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5010图书馆幽灵封印研究会第2型.png",
        ),
        _p(
            name="图书馆幽灵封印研究会第2型",
            subtitle="物理武士刀-攻速",
            notes="奇迹：猎人/情报官",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzj++/xXUD2HjgbZwiy1KXlBiC7ZCR3YUEsFnxMSjwXqT6uYxX4UeyjT+BXj8j85rzzUToHR8ix/ulcBvBEsfuE1i+elJqAXei3SlCqBm344jdQVrkyS334PlUsEFFxFZY4NGzNdetlvVRlmlTawma8A+tqYnLUh3MG2gE2PIR1d+N0ou4UreEJhjm95FXNKQI44DltkC4z+mdQI+SUMcfX4KaD14a6xb7u2fT7mt9gkpbP2gCAkQjOT6urkKDjXaxOSUENe2R5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5010图书馆幽灵封印研究会第2型.png",
            author="梅子黄时雨",
        ),
        _p(
            name="永霜的沉默",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzznhwuxXUA2inGY/VdT6yZMuaxBC1NMwB5kf0X/b9jq2puHuMYwRPQYuJ8LmgzjXw7NBTF4GBISpgkwn4yaPigD4C6p+b7EnC9HNKnv8Gvc0VVB/j2PENlLqFDu+jbSDUhfpJ1+DNBnbPNxx5p8mdlyrhoJWg4xEUmAzrmAq0a8FHk3uIJCIi815b7OQjnni39bv/DNNYMFrOZDQFqvGunyQN+/kIGX3bbtj4qGvCCSu21IcYp7Q2BybQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5011永霜的沉默.png",
        ),
        _p(
            name="纳斯特朗的碎片",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzi+2uxXVz2EvC6UFWh1Bmi1ieDAsNAqEYKNwxu3/ciO5s4NIqXke5raTnyYNf9yWTp426nnybBXb1VAg5FgIHkqMqW1jkOWpl8PeeqUvFXaIT2Z6T85NZvaYZGQs4r5YCmQc+2NPd5KX4+jIHpE6gAWQPhVHBple2BWDlc3ca79ovY28UKadS3O88g0QmchBw++cl88/maScX6jCYdv513Ha7LCp6irLplo8aZr8ERsad+tKi3/G9zbVA="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5012纳斯特朗的碎片.png",
        ),
        _p(
            name="电光一刻",
            subtitle="魔法科技",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTiC2qwXVz0ivab50b6H8Ve3ryQIfgXchf4iFJjk57v70OaiLGb/kcsPkAaF/t/y9Zf96yz9NxLG7bct8R7XsVmt/BnuywkLDT9uFYL/EgJlyVwPXrsMmpGZqk8wWvXRyAi5ec8I2Ell7sJzm/zWEsyOr92OyRTCuvW1DH1b/S9EalE/rz826oeWgIK3YWoHSQZX8dZyQLboIeGwum9Jm2yoMCXFQGTST6PFYSIaW9u"
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5013电光一刻.png",
        ),
        _p(
            name="破甲刀",
            subtitle="物理武士刀-非攻速/守护",
            notes="奇迹：侍卫",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnh2uwXVzyhAjEG4Eqs0SOkfiz59G/dfJMXzmOreJkhZa1exSC9exK9ddYQxVyJGVBKh6s98CD/6pQyKb39agZICTBTjnN+MCuyThfG0UICMg6WbS0KaCfcyD9BtFEygZXPBv5NDbJZQHRYs99K+PmG8xCZUTDVHrRV2tof4TKWfscl/+bc80q1yBG3K3F0mUCP1b1Lo2Wdp0B4evE+omGJI1WX150B4x5QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "katana" / "5014破甲刀.png",
        ),
    ],
    "长棍": [
        _p(
            name="大力棍",
            subtitle="物理长棍-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnjWvxXUA3kvKZPVFbUENqHMfM+TJFRMolIhsyBZwT3OAghTJ8gr2p2bhhWMlgSKUgUtmTAhRxjBwZe2KO8EvfWskGlyHeFsQWKDtPFMuRF9ifrq03Vn7FeGkiV9PTm1LnYHEDYMnEdSplWw0eqTnOlQNiBKmwedU8FngTR891VFSrrnOZupYJRZQL3LjPqYVJ9hABjlnwuRToIh1tngLFrlTlSCeLrmV5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6001大力棍.png",
        ),
        _p(
            name="大力棍",
            subtitle="太阳剑",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhC2rxXVz0ivabZ1ghXsaz2A18gEwA2RzpS9XnkB76jm8R+tdVrOjB2kT8g2x5y3E0qf3byiYBaNjpYhou1/1wYgqrgd8vc88ClkyARRNyzzXO6T96WOy+YVPYI+fIbVZg6RauR2eoXAXkaY1l2kQct19Scfq6+49Chwdox8LzEfU/GQOQ7CYJnFJQl9PY2IbZP/ABnYodzgLuA6Uyu36QbOST3cQaznFm3+SIJmxvQW4="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6001大力棍.png",
        ),
        _p(
            name="大力棍",
            subtitle="太阳剑-陨铁护肩回收",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzgC2rxXVwyivabZ1ghDMezGLRzwzycqRzpS9XnkB76PnvJUQ7hg/bV1EfT1nI3f9sC/KxSFMu2fVCkaATeTH0aCMJHT+4V3ZDRNSpdRz1DqF82MAlmD12hvTV1rHNqJZh/PuIEem/bVppuEa6fSflbGzF2C0C3CXuGzOAmzQGZsO7HCJ4extY9tte/57yOEM2r7qlI4xAWwuDOdpJq0g47r+zvdS1qaNOAv2N0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6001大力棍.png",
        ),
        _p(
            name="大力棍",
            subtitle="行星",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzziC2rxXVz0ivabZ1ghDdmz2M1igzMlCAgbO7QAAZ4Tzw1+GykKl5XmYBbnOy/mSLXTTbCfmNMBG+NImNHCdxjBAWcVyfS4uEqlp0m/GL+Ez6jevEZO4eV5/+X91OF/rFnOhVs28p5KRfln1cZ9RTGyP+PpIv6lcIFqfEa01hSOOGwJMMMPY5ZTDDBJuVru8oAL7Oi5Muva2FmPpADlqKsRmcw3+sR/8JNVOgxpkcc8TG9pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6001大力棍.png",
        ),
        _p(
            name="大力棍",
            subtitle="行星余烬",
            notes="奇迹：天文学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyTiB27wXVz3ijiTOwu69weld0QbA8E8qavdYfJVdJyT8CWxiAutHpi+vuErChz0SsnQo5aHE1AJKujxavnK0uNpildJehMUg9GGT0JIckgYgBLGj3d/0X1tPwX1Zkb3IVjSBTY12A1GQfdKWUGNQ+x+MMxiVUQ6YFM1DbZkwsJHAD5uWTY+SCchuZJXu+cUPkc+r+Yc5W8Ts1qFEpPoWwXCxv7HgxwmFDK0kT8u8ISd/4DevvtD1z2Df3RzZXM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6001大力棍.png",
        ),
        _p(
            name="精灵融合杖伊洛妮卡",
            subtitle="火焰魔弹单核",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzgh2vxXVz0ivbbPVjhDB7IbMJ3fdv9d6ngXESFV5eSavBvUaQZJ42aH8lh1AhBSbXTDLSDDgSdFsVMjKqDVlMr5QAq+rq+yJIGtmoWAtUDYc0oei1mR09/b/98xoBZK3TxYAkjdFIaxeY5O2fHIxrUfSvg+U2lxnLnRQ9S54S55Lc3xVMhrVboEwxMZAx+waY+HJ8qiSzHaDiOFuXotkeSmeNklumk8XpWvB+O8tmHu58Q89WWR43E01BpZHNl"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6002精灵融合杖伊洛妮卡.png",
        ),
        _p(
            name="精灵融合杖伊洛妮卡",
            subtitle="寒冰魔弹单核",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTg+2+wXVz2kjsc5xXastYsmExTRDaWzkVtIyLyTdBOYP9sdmGyhTwCq6oK/SLvANV5E5eVGxDLBvC6373zFP3xNgcZ97xPqSE5x5Iosvk4qPEGR4fe7TfjACEc6COC9xF4KDiF7yWoIUB/PTi08YdCdltiDt71xmzrrzdxXbj/D8vq+RzMtG7T97fit85gOl/7x6A/2woFVgjhD0NmG7jA7JBcbo8dVSq+S9ipV5mNcZHAtaahNtmMR3msqWMISUxpYXI="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6002精灵融合杖伊洛妮卡.png",
        ),
        _p(
            name="精灵融合杖伊洛妮卡",
            subtitle="闪电魔弹单核",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTh+2+wXVz2kjsc5xfa8koa1scr4WAkaH0MBStZT5CSRVdCrcA9gsCKponsO+9PSg2sloaHGLiEEU21797VKtBKClMT0Uo6tJV8XL9rrI4l9Tki7ftiAxhrO3nmB/Yy7VIrITKXdrH7mTRxL1uIwLZTqPFpUR7/IJckUOR5/XQ0Nzx3v6+XNfEUm/TY75M3jSbFBNuRQLYGGcaPvd/1FMRQrD6yC05rtp8m991Z76KXFgecb9JucORrbFBy"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6002精灵融合杖伊洛妮卡.png",
        ),
        _p(
            name="精灵融合杖伊洛妮卡",
            subtitle="三魔弹音叉核",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzgDWqwXUD2ivKZ51UekjwfQVA7gCTF6xeaEC+Zz4GTMdYKfV+L/aqpOHprKwOtRSXzb+y7npKb23A74ZjKC/tcyvuARNHXdd9SLBIwA4Nl4yAL2Px6iuIJDuJ8ekJCf3EYYyrREIL7tHN9g4VlnkNs74ymTaHJUAxAoalobVanddrDafxMi9AWJ8ZtAtX5AnLTlQYBfOg+atOw64pmCBQgg/y6VVagZWrCm5YX1rK+BjO8GLyAjYs9+v5ej4md3/eQYZqzi5BBQGN0"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6002精灵融合杖伊洛妮卡.png",
        ),
        _p(
            name="精灵融合杖伊洛妮卡",
            subtitle="魔法书-书库之阳",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzQiC2qwXVzPaoUqIhuyB5/fGLxDUZWxT+epy2Q3qJ7jj5GQzN/lkuJRskajg2Bt60nDcd+q5kERiwxmFdIjNvhmFYC4A8FPS7PBj6yC0YUXwNtGbWuJa2rGaPnNK0umY1TiUBRh/N6S4Sil+A7VBRtAaW1yl0pc/2RhqVK6d0L7E0ehQY+49z3KijOtU9zSu78cF92zauTTEkqelQMrCRJ9l8eeqsCQp5l08OgJ88Gil0McypzYiq2h9fZG+pBNgXxiJzaKbGR5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6002精灵融合杖伊洛妮卡.png",
        ),
        _p(
            name="海之锚",
            subtitle="物理长棍-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXUA2ivKZPVHTUKNB1SESsMEWM8spIpszBZwT/MDXvZNMu39JJwZLE0QeSKUgrLizGhRztBwZe12O8EvfWkkHESG+GMQG6CNP3MoRlgGjnurdl01BTnHmxAFTLHUiIZ5tQkTAazolCcPqEPR1Tcug0c9YpE0L5baw+ca8bHZAVsLbpzmZZfFm4ma6T3BAlsfQPJr//4rpXaSVGm7CJ47tD5q2kH7Lp7npkG9uQQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6003海之锚.png",
        ),
        _p(
            name="海之锚",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSnC2uwXUD0hA4FGoGoLegMNd9T5+kkAgb7o9jPc6GXaf3yZT4se00Dzj1KMRkBDzX+2ZWJZAXnbqnkLKoWOWfRQDemBNjWQkhJGrj8ydlkYsIHfM5ZZEzbLIP3zO2xf8Km0zvTbuIsVxDzxljRaOnEZPqv1yZjRyQhmYLEZe16sW/yry4mbisao+KHk+zDB3/Bpl9EupCYATFtVDGwPpFldFM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6003海之锚.png",
        ),
        _p(
            name="无环锡杖",
            subtitle="坚固风之歌",
            notes="奇迹：决斗家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSgB2uwXUD3hA5FQxoIB+gM0REsDXbVv71EhAMkUOGbGVlzfIyOGU9Dnelh1ChGSA0MyQqrtjVDsIvQSxEAsQZShmjxaCjwWT5gvRKrU4GgcEEMBn90a3/IZmelBWg4Rwcmft9lPjcrB6vdmg/zYwv3SAd/5DTMBZAXmncjQG8ZULSAAsy7IqR6scTGtYDZcquFOCKiGF2RF8p9OvYE8K5ldFM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6004无环锡杖.png",
        ),
        _p(
            name="圣海碎片",
            subtitle="物理长棍-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnh2uwXVwyivKZPdYMCh/y1qNPIEtOUwqCqS4ZmpxTYEHw6mysLju2+N9YKlInIwAHLphfVrgbmn9PLFllFe38REV0UIXwl3H64GdMYi8WOFcc/yto+mhcY6BAZ+2QMBEHF9LLAMvdcUhcu5JwYKgAFosAMDKWCa0RfS2xgPoMDL2Yi1mJYqYWgea8QWN0"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6005圣海碎片.png",
        ),
        _p(
            name="突击枪卢阿施蕾娅",
            subtitle="物理长棍-攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTnh2uwLVw2ivKZvVmh18NQdvAv5PTChUWr4muos5qT3uF6c7aD4xK/AjXsJPdt6rac/I7bnTO5LCmh5xE94Mt4ISUG/QIcfk+tC96tiuPbNVhOBULmXVDhdOrUk2nB+3EgRjL/59axezDKTJvnUfGSslKbzq6kIvcNqpJGM68HK5QLvJBcm59m1Z6A5qt0aW8="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6006突击枪卢阿施蕾娅.png",
        ),
        _p(
            name="突击枪普阿尔斯卡",
            subtitle="物理长棍-非攻速",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTih2vxXVz0ivLZPVQh1CGO4g1+wxAmdN2NJXAftCCw2B5bdtNvn4LACyxyhggj08lYA8vY0tL4hpg1+lQwoZjMTFxkhBP87EY793sXVkS/KMIscnYbB3+bKUYF8hz2yVkjIX/pbEhLvD1IDI0U61fhL/bc0U02BbjO8FqMW0HweLUW3Hziqu2RijK0kf9OGLCU4oEvup+zZd1zfYRCT6pldFM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6007突击枪普阿尔斯卡.png",
        ),
        _p(
            name="突击枪普阿尔斯卡",
            subtitle="物理长棍-非攻速（白狼）",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzSge2rxXUDyhE71CzGIT63s2A0iHTc44ht6zdo5hbOTCRJ86H5dKl2sQZ7s/V+0SxWvh4aFlYuLvLRQJrAKw/nnfgbf/qMrEbIfiLYDJ+NU7b3UioNyUH5CaYYm+sVmzF5nL3TxBnj9R6tvXmX8J8V85EZRz6mvHlcpGyjabrWqrypycdImVHsmQgIKDbSvtbKltekAU9QRrKbTFbn1S/6mkdz0HHOMNGqNsGN0aQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6007突击枪普阿尔斯卡.png",
        ),
        _p(
            name="皮亚奥拉议事槌",
            subtitle="余烬",
            notes="奇迹：厨师",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbb/dbMV8Sz2BZsR4kwblQZ6d6CtZrfQqcS+n9tWgz3ws45yglBS8jDmVwrEvixG8N4co9s2agybTsuQxSXetSxI7pwioP5Ocb7YbF5Sa9jtbFqwMp52QhAWXv1JWmhpQ4wK2xZfKo85SdCKVsuOjkELODGlJtLf4+7H5domPIzACmaaE5ol4n+h1q0t+ARGDMFNH+ljKzQjlMs9iUpv2V5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6008皮亚奥拉议事槌.png",
        ),
        _p(
            name="索利斯·布拉卡",
            subtitle="太阳剑",
            notes="奇迹：猎人/陨铁铁匠",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhjWvxXUA3kvKZ/dLxXUaj3g19gHQugVUrxAAikv6iDnbX9pPr3AT3zg046wkVSzdN4BjK50nT5LZrU41lAxN4UTgX9sBPaSPCvInxcL1UeVmday0/JWY3Xqm80HiYb0g6VeVIu4Nojq5g4X3dVf6XuHxa3ncnYPTZ46blDWN/MLqFQv6ywYI+4r3XbsYsqt2o57GTFMOMkYJiqmivj/LZb7lZD4UcJpp/aF3moxOrSW9pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6009索利斯·布拉卡.png",
        ),
        _p(
            name="巫女的预言",
            subtitle="冰霜武具",
            notes="奇迹：冰锻造师/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzgB2rxXVz3ivab50X6u9w/BIdPUOU+dBeALWnS4/yarfYKt3Fdujgd27h+9RBuRSXzfw/bBhWJ2XDmuibmc5kPGmanPNQCWol+HZhfLLXf5f9/E0MV14xzfd07TtQTTBKp9YOodMIpQcMJdvY+u1nSo91TaMJpVaeaPllcHd7aW9l/XcUI9POzYrJPdeuQzVdpjAN8+Cp9hRGZl6FgcMW+TM6/GGht5BQnrhwP4PgQHakQj61jUulc31NzZXM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6010巫女的预言.png",
        ),
        _p(
            name="马拉斯皮纳",
            subtitle="冰川",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzzhh2uwXVz0ivbbPVghtqi/1qPVc/sHJQ6JL4MJOpCIlboKfOwOGYoa5mel6e6oFWYJl5kNFqgJ24zbgU6iqL/cxoGjQGrS4Pam2TvyWS3sIiltRIlbMBifZbdmQsZ6qABtblsmc1H9nHDMe2D/hyljyc2MYd5rzfdeLLBqX5erjcZVwUBiixF0jwfl3N/QAjoXgreNQhy/MABgNa8e+TG+qeizkZXERLJJffnqP1DPrHNRbWBsRg=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6011马拉斯皮纳.png",
        ),
        _p(
            name="比杜卡",
            subtitle="魔法科技",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi/WuwLUA3nvaY53+kjUn+IexiTEdFre/bBQxAlZ7pdbsaHmiuHJVZ10e/hXLBIzaOO13Q0Uth+lvS42sH6/QHhQX+UiNbDLBe7KkY4MCRU2HuY05qA7plX9UZw7tCb2DiV2xdxze3rSUNy6hokVrGIUSJJUVkIKws3MLdYxnDldLjmWBOpOCD7tGE5Fw7PXed8DEiFpu7dPXDITtsrQzf0StrCKws6ZJ5QWM="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6012比杜卡.png",
        ),
        _p(
            name="内波拉克斯",
            subtitle="乌云",
            notes="奇迹：猎人/气象学家",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThh2vxXVz0ivbbPVjhDCg+BMd3JS0xXhn4qAcK1o2RH0tJAdcOGQwbNpkaJVvL2mXd6YEItnG1upv9D++q/VSWFYNz6aZT5IDR0Pk7OzgVmavwvCQfyWbxRmUvSvq+VNa9dwWWfRJJB3tkXgMCKm8zi+dw0x9iKTPgl0tY5XfaaXkh0kcdtYoYGEFKgSQmJR7y28T0tsCL5IjoPoPtrv2YAwz/ssOPzS6ErjEIaTQFAF1pbGFs"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6013内波拉克斯.png",
            author="Eden_T",
        ),
        _p(
            name="神圣之壶",
            subtitle="物理长棍-攻速",
            notes="奇迹：将军",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTgjWvxXUA3kvKZPVFbUENqHMfM+TJFRMolIhsyBZwTfOAghTJ8gr3O2nSMjWRpSwI0qf3bhBJaiq8wYem37NWsCYK7Lp7vKalNRNsZ8scirM1rYggzAT43TTknNkvxYVtSDWnF0/tEBVLEm7wzAHjk+BRIbnUqa0srgbhm2QAifBJPO9Yg6MFTA5lHpg96mB3zmtWph0bbOAmRVcyNEOkqOUyTELoCVLrVZBmAaW9u"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6014神圣之壶.png",
        ),
        _p(
            name="无形之舞",
            subtitle="物理长棍-攻速/影子",
            notes="奇迹：盗贼/猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZ1znjWuwXUA3kvKZPVFb8rZRos8jXr7ATDrkirgfjCctQh6tYdj5XO9e4wg9XDhUDWJZhE0aNqChYiOaER4ndyU9i2aR3xvHEYYeFNomSsHeVP51gkLu1Ix5fN07TmRA5cFRv9P1SGPQactFKFwXWdpBaeOy06Xvo9B5FJWjR9KgTCTjCNtRKCMixtroVUp6jiTE7mSi0u0hHW4vFrStzNneRRj3l8kDI9/vBjxYWDYDrm5pbQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6015无形之舞.png",
        ),
        _p(
            name="继承者",
            subtitle="火焰法师",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTh/W+wXVw3kjuc5xXavMYUmcztw3v0w2Pm8HvAtXmMueS/DjBLlAaJl+V1segW4WXVqLGCHxBS7FfMUZBZ0mFcIoOeWbaguSoOZgOsMvygcraiBX0sSWtr/iNGQnGKRbDYJXnFNKplc8Mb6DMJYBlmye0qAcu+NYvqyvXY//xMSs4vIQKO0SBW+pOh20KN68/nS7oiu83/he5sdtet3qXp3YzHmyP/9NKUmxbL1pM7grYe1rKCPrHnegm49stFdVNo"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6016继承者.png",
        ),
        _p(
            name="继承者",
            subtitle="冰霜法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzThC6qwXUD2ivKZ51Ue1huWqkyta2YJtj1ho9+seQ5ysp4RK1SDl0Opup/OVcAzrL1pKLaxlIKQOQQc5xiaETZh9Gy97sJ3IuCMpGlvIKuSo87jP8QzJRzHD5NuUqREeZBhInPy9zjitsy0SdvTCGvcaLt0xQXiK+j4gWERYo6Jf3fcxnGKgHNbI1A/GmoZa68W5rtfd59AKW0N8ztHoI5EARBXdInOGfLPvJKGyqnHrui6nZ7rnGrJH1p8QXJldA=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6016继承者.png",
        ),
        _p(
            name="继承者",
            subtitle="闪电法师",
            notes="奇迹：猎人（开局丢火焰箭）",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZzTi+w+xXVz2EnIfZ1hISLufukFBD4m1xP56SVyz5e0AX7OFKpkKDORq84CZL9ep47BMOmPZkxMUfTFWNzweG4NPNVAh8hZQ+oEOt8gjSAzSNDjX4rsENKJhTFVk12XevfV0TPNlrVj23IToHXViSut4gldMAWAyTRjc6/1DFQiyYJfAXiJVGxxEhdTrTKz+C70Ej8BIhfNsIzLZLmbKahKiHqzpN5VZ3raBfJdrhZD/5EHuDNuRFZILhZe5nYZM8+w/HhY4bWR5QQ=="
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6016继承者.png",
        ),
        _p(
            name="继承者",
            subtitle="双发回旋镖",
            notes="奇迹：猎人",
            preset_code=(
                "AAF_PRESET_OBFZ|v1Xuh8aW9uQW5pZyzjiyt2XED2ivLZPVG1/I2pYqm3q8PfqoHsOfr4mEmUuGbZeJEx22fwmrmmeWk+uLdq0FYHVhETPzYahPgCd73WFz5QW1WryoVfk8uB2xOYvB4bv3NVEkfnxOtuzAIBQdVmadxBDKpvOCM4awNZBfdccarvBXEru1dMVkhiTRnRf5FcVRY4ZtdWWfEtbdKBgb06MPR69/FCvqvTlu9DdqcK0GaPH2gSoBDgroKL+gxwxoudZ5RUWHcutinrsrifiPc1vpGT2E1cQGN0"
            ),
            icon_path=WEAPON_ICON_DIR / "staff" / "6016继承者.png",
        ),
    ],
}


PRESET_CATEGORIES = ("看前须知", *PRESET_DATA.keys())


def query_value(name: str) -> str | None:
    value = st.query_params.get(name)
    if isinstance(value, list):
        return value[0] if value else None
    return value


st.title("预设合集")
st.caption("赛菲莉娅 Sephiria / 可复制预设码资料库")
show_last_updated(WEAPON_ICON_DIR)

requested_category = query_value("category")

selected_category = st.segmented_control(
    "预设分类",
    PRESET_CATEGORIES,
    default=requested_category if requested_category in PRESET_CATEGORIES else "看前须知",
)

if selected_category == "看前须知":
    st.subheader("使用说明")
    st.info(
        "这里收集可直接复制到游戏内使用的预设码。每张预设卡会标注武器、"
        "玩法方向和适用说明；复制完整预设码后,在游戏内导入即可。"
    )
    st.caption("预设会按武器分类整理。请选择上方武器分类查看对应内容。")
    st.divider()
    with st.expander("如何添加 / 修改预设?"):
        st.markdown(
            """
            直接编辑 `pages/5_presets.py` 中的 `PRESET_DATA` 字典即可,推荐用 `_p(name, subtitle, icon_path, preset_code=..., notes="")` 辅助函数来构造每条预设(默认 author=`DFM05`、version=`1.0`,无需手动填)。

            重要约定:
            - **按武器编号升序排列**:同一武器分类下的预设,按对应文件名里的编号(剑盾 1001… / 大剑 2001… / 匕首 3001… / 弩 4001… / 武士刀 5001… / 长棍 6001…)由小到大插入。
            - **同一把武器可有多张预设**:在 list 里追加新的 `_p(...)` 项即可,不需要做去重。
            - **作者统一为 DFM05,版本统一为 1.0**:`_p` 辅助函数已自带默认值,通常不再需要单独声明。

            每条预设支持的完整字段列表(仅供覆盖默认值或特殊情况时参考):
            - `name`: 预设标题(必选)
            - `subtitle`: 副标题一句话简介(必选)
            - `preset_code`: 完整预设码字符串(必选)
            - `icon_path`: 图标 PNG 的绝对或相对 Path;推荐使用 `WEAPON_ICON_DIR / "<武器标识>/<文件名>.png"` 指向已同步到站里的武器改造图标,文件不存在时会自动退化为文字占位(可选)
            - `icon_text`: 图标文件缺失时显示的 1~2 字占位(可选)
            - `author`: 作者名(可选,默认 `DFM05`)
            - `version`: 适用版本号(可选,默认 `1.0`)
            - `notes`: 补充说明(可选,副标题下以灰色小字显示)

            武器图标已全部按「图鉴/武器/2阶改造（小）」的目录登记到 `asset_manifest.json`,目标为 `assets/wiki/presets/weapons/<武器标识>/<编号+名称>.png`。武器标识对照:剑盾=`sword_shield`、大剑=`greatsword`、匕首=`dagger`、弩=`crossbow`、武士刀=`katana`、长棍=`staff`。后续如果源图有更新,运行 `uv run python sync_assets.py` 即可同步。
            """
        )
else:
    st.subheader(f"{selected_category}预设")
    st.caption("以下预设示例码为占位串,请替换为真实预设码。")
    render_preset_grid(PRESET_DATA[selected_category], columns=2)
