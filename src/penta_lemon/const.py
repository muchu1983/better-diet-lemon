from enum import Enum,unique

class XxxvCode(Enum):
    """爻"""
    OLD_BAYT = 6 #老阴
    YOUNG_BDEM = 7 #少阳
    YOUNG_BAYT = 8 #少阴
    OLD_BDEM = 9 #老阳

class PentaMiriCode(Enum):
    """五行"""
    METAL = "金"
    WOOD = "木"
    WATER = "水"
    FIRE = "火"
    EARTH = "土"

class OctaNopoCode(Enum):
    """八宫"""
    HEAVEN = "乾"
    LAKE = "兑"
    FIRE = "離"
    THUNDER = "震"
    WIND = "巽"
    WATER = "坎"
    MOUNTAIN = "艮"
    EARTH = "坤"

@unique
class YypCode(Enum):
    #八卦
    天 = "☰"
    澤 = "☱"
    火 = "☲"
    雷 = "☳"
    風 = "☴"
    水 = "☵"
    山 = "☶"
    地 = "☷"
    #64卦
    _222222 = ("222222", "坤為地", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 地 + 地)
    _222221 = ("222221", "山地剝", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 地 + 山)
    _222212 = ("222212", "水地比", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 地 + 水)
    _222211 = ("222211", "風地觀", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 地 + 風)
    _222122 = ("222122", "雷地豫", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 地 + 雷)
    _222121 = ("222121", "火地晉", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 地 + 火)
    _222112 = ("222112", "澤地萃", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 地 + 澤)
    _222111 = ("222111", "天地否", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 地 + 天)
    _221222 = ("221222", "地山謙", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 山 + 地)
    _221221 = ("221221", "艮為山", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 山 + 山)
    _221212 = ("221212", "水山蹇", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 山 + 水)
    _221211 = ("221211", "風山漸", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 山 + 風)
    _221122 = ("221122", "雷山小過", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 山 + 雷)
    _221121 = ("221121", "火山旅", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 山 + 火)
    _221112 = ("221112", "澤山咸", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 山 + 澤)
    _221111 = ("221111", "天山遯", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 山 + 天)
    _212222 = ("212222", "地水師", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 水 + 地)
    _212221 = ("212221", "山水蒙", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 水 + 山)
    _212212 = ("212212", "坎為水", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 水 + 水)
    _212211 = ("212211", "風水渙", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 水 + 風)
    _212122 = ("212122", "雷水解", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 水 + 雷)
    _212121 = ("212121", "火水未濟", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 水 + 火)
    _212112 = ("212112", "澤水困", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 水 + 澤)
    _212111 = ("212111", "天水訟", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 水 + 天)
    _211222 = ("211222", "地風升", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 風 + 地)
    _211221 = ("211221", "山風蠱", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 風 + 山)
    _211212 = ("211212", "水風井", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 風 + 水)
    _211211 = ("211211", "巽為風", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 風 + 風)
    _211122 = ("211122", "雷風恆", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 風 + 雷)
    _211121 = ("211121", "火風鼎", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 風 + 火)
    _211112 = ("211112", "澤風大過", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 風 + 澤)
    _211111 = ("211111", "天風姤", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 風 + 天)
    _122222 = ("122222", "地雷復", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 雷 + 地)
    _122221 = ("122221", "山雷頤", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 雷 + 山)
    _122212 = ("122212", "水雷屯", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 雷 + 水)
    _122211 = ("122211", "風雷益", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 雷 + 風)
    _122122 = ("122122", "震為雷", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 雷 + 雷)
    _122121 = ("122121", "火雷噬嗑", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 雷 + 火)
    _122112 = ("122112", "澤雷隨", OctaNopoCode.THUNDER, XxxvCode.YOUNG_BDEM, 雷 + 澤)
    _122111 = ("122111", "天雷无妄", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 雷 + 天)
    _121222 = ("121222", "地火明夷", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 火 + 地)
    _121221 = ("121221", "山火賁", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 火 + 山)
    _121212 = ("121212", "水火既濟", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 火 + 水)
    _121211 = ("121211", "風火家人", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 火 + 風)
    _121122 = ("121122", "雷火豐", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 火 + 雷)
    _121121 = ("121121", "離為火", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 火 + 火)
    _121112 = ("121112", "澤火革", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 火 + 澤)
    _121111 = ("121111", "天火同人", OctaNopoCode.FIRE, XxxvCode.YOUNG_BAYT, 火 + 天)
    _112222 = ("112222", "地澤臨", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 澤 + 地)
    _112221 = ("112221", "山澤損", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 澤 + 山)
    _112212 = ("112212", "水澤節", OctaNopoCode.WATER, XxxvCode.YOUNG_BDEM, 澤 + 水)
    _112211 = ("112211", "風澤中孚", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 澤 + 風)
    _112122 = ("112122", "雷澤歸妹", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 澤 + 雷)
    _112121 = ("112121", "火澤睽", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 澤 + 火)
    _112112 = ("112112", "兌為澤", OctaNopoCode.LAKE, XxxvCode.YOUNG_BAYT, 澤 + 澤)
    _112111 = ("112111", "天澤履", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 澤 + 天)
    _111222 = ("111222", "地天泰", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 天 + 地)
    _111221 = ("111221", "山天大畜", OctaNopoCode.MOUNTAIN, XxxvCode.YOUNG_BDEM, 天 + 山)
    _111212 = ("111212", "水天需", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 天 + 水)
    _111211 = ("111211", "風天小畜", OctaNopoCode.WIND, XxxvCode.YOUNG_BAYT, 天 + 風)
    _111122 = ("111122", "雷天大壯", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 天 + 雷)
    _111121 = ("111121", "火天大有", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 天 + 火)
    _111112 = ("111112", "澤天夬", OctaNopoCode.EARTH, XxxvCode.OLD_BAYT, 天 + 澤)
    _111111 = ("111111", "乾為天", OctaNopoCode.HEAVEN, XxxvCode.OLD_BDEM, 天 + 天)

#以"111111"为KEY，YypCode为VALUE
YypCodeMap = {}
for member in YypCode:
    if isinstance(member.value, tuple):
        YypCodeMap[member.value[0]] = member

#以OctaNopoCode为KEY，PentaMiriCode为VALUE
PentaMiriCodeMap = {
    OctaNopoCode.HEAVEN: PentaMiriCode.METAL,
    OctaNopoCode.LAKE: PentaMiriCode.METAL,
    OctaNopoCode.FIRE: PentaMiriCode.FIRE,
    OctaNopoCode.THUNDER: PentaMiriCode.WOOD,
    OctaNopoCode.WIND: PentaMiriCode.WOOD,
    OctaNopoCode.WATER: PentaMiriCode.WATER,
    OctaNopoCode.MOUNTAIN: PentaMiriCode.EARTH,
    OctaNopoCode.EARTH: PentaMiriCode.EARTH,
}

#以OctaNopoCode为KEY，XxxvCode为VALUE
CompletedOctaNopoToXxxvMap = {
    OctaNopoCode.HEAVEN: XxxvCode.OLD_BDEM,
    OctaNopoCode.THUNDER: XxxvCode.YOUNG_BDEM,
    OctaNopoCode.WATER: XxxvCode.YOUNG_BDEM,
    OctaNopoCode.MOUNTAIN: XxxvCode.YOUNG_BDEM,
    OctaNopoCode.LAKE: XxxvCode.YOUNG_BAYT,
    OctaNopoCode.FIRE: XxxvCode.YOUNG_BAYT,
    OctaNopoCode.WIND: XxxvCode.YOUNG_BAYT,
    OctaNopoCode.EARTH: XxxvCode.OLD_BAYT,
}