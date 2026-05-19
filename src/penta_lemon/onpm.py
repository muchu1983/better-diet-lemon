from penta_lemon.core import Xxxv
from penta_lemon.const import XxxvCode, YypCode, OctaNopoCode, PentaMiriCode, YypCodeMap, PentaMiriCodeMap

class OctaNopoPentaMiri:
    """八宫五行：64卦归八宫五行"""
    def __init__(self):
        self.pentaMiriCode = None
        self.octaNopoCode = None
        self.yyp = None

    #64卦归八宫五行
    def assignYypToPentaMiri(self, yyp):
        if yyp.isCompleted():
            self.yyp = yyp
            #查出该卦的所属八宫及八宫对应的五行
            yypId = self.findYypId()
            self.octaNopoCode = YypCodeMap[yypId].value[2]
            self.pentaMiriCode = self.findPentaMiriCode()
        else:
            self.clear()

    #8宫五行卦转爻(进位) 6进制但每一位有64值域
    def completedYypToXvvv(self) -> Xxxv|None:
        if self.yyp.isCompleted():
            pass
            return Xxxv(XxxvCode.YOUNG_BDEM)
        else:
            self.clear()
            return None

    #清除状态
    def clear(self):
        self.yyp = None
        self.octaNopoCode = None
        self.pentaMiriCode = None

    #六爻阴阳 找出 卦id
    def findYypId(self):
        yypIdChars = []
        for xxxv in self.yyp.sixXxxv:
            xxxvCode = xxxv.xxxvCode
            if xxxvCode is XxxvCode.OLD_BDEM or xxxvCode is XxxvCode.YOUNG_BDEM:
                yypIdChars.append("1")
            elif xxxvCode is XxxvCode.OLD_BAYT or xxxvCode is XxxvCode.YOUNG_BAYT:
                yypIdChars.append("2")
            else:
                yypIdChars.append("e")
        yypId = "".join(yypIdChars)
        return yypId

    #八宫 找出 五行
    def findPentaMiriCode(self):
        pentaMiriCode = PentaMiriCodeMap[self.octaNopoCode]
        return pentaMiriCode

