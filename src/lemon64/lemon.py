from lemon64.core import Xxxv, Yyp
from lemon64.onpm import OctaNopoPentaMiri
from lemon64.const import XxxvCode

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
