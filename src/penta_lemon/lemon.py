from penta_lemon.core import Xxxv, Yyp
from penta_lemon.onpm import OctaNopoPentaMiri
from penta_lemon.const import XxxvCode

class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.octaNopoPentaMiri = OctaNopoPentaMiri()

    def __str__(self):
        return self.yyp.getYypId()

    def feedXxxv(self, xxxv):
        self.yyp.append_xxxv(xxxv)
        self.octaNopoPentaMiri.assignYypToPentaMiri(self.yyp)

    def getCarryXxxv(self) -> Xxxv:
        if self.yyp.isCompleted():
            return self.octaNopoPentaMiri.completedYypToXvvv()
        else:
            return None
