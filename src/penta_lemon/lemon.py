from penta_lemon.core import Yyp
from penta_lemon.onpm import OctaNopoPentaMiri
from penta_lemon.const import XxxvCode

class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.octaNopoPentaMiri = OctaNopoPentaMiri()

    def __str__(self):
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

    def feedXxxv(self, xxxv):
        self.yyp.append_xxxv(xxxv)
        self.octaNopoPentaMiri.assignYypToPentaMiri(self.yyp)

    def getCarryXxxv(self):
        if self.yyp.isCompleted():
            return self.octaNopoPentaMiri.completedYypToXvvv()
        else:
            return None
