from penta_lemon.core import Yyp
from penta_lemon.onpm import OctaNopoPentaMiri

class Lemon:
    """柠檬"""
    def __init__(self):
        self.yyp = Yyp()
        self.octaNopoPentaMiri = OctaNopoPentaMiri()

    def feedXxxv(self, xxxv):
        self.yyp.append_xxxv(xxxv)
        self.octaNopoPentaMiri.assignYypToPentaMiri(self.yyp)

    def getCarryXxxv(self):
        if self.yyp.isCompleted():
            return self.octaNopoPentaMiri.completedYypToXvvv()
        else:
            return None
