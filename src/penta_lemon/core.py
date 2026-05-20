from penta_lemon.const import XxxvCode
"""核心类"""
class Xxxv:
    """爻：万物分阴阳"""
    def __init__(self, xxxv_code:XxxvCode):
        self.xxxvCode = xxxv_code

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻

    def append_xxxv(self, xxxv):
        if len(self.sixXxxv) >= 6:
            self.sixXxxv.clear() #清空重来
        self.sixXxxv.append(xxxv)
    
    def isCompleted(self):
        return True if len(self.sixXxxv) == 6 else False

    def getYypId(self) -> str:
        yypIdChars = []
        for xxxv in self.sixXxxv:
            xxxvCode = xxxv.xxxvCode
            if xxxvCode is XxxvCode.OLD_BDEM or xxxvCode is XxxvCode.YOUNG_BDEM:
                yypIdChars.append("1")
            elif xxxvCode is XxxvCode.OLD_BAYT or xxxvCode is XxxvCode.YOUNG_BAYT:
                yypIdChars.append("2")
            else:
                yypIdChars.append("e")
        yypId = "".join(yypIdChars)
        return yypId

    
        

