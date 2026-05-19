from penta_lemon.core import Xxxv
from penta_lemon.const import XxxvCode, OctaNopoCode, PentaMiriCode

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
            pass #查出该卦的所属八宫及八宫对应的五行
            self.octaNopoCode = OctaNopoCode.HEAVEN
            self.pentaMiriCode = PentaMiriCode.FIRE
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