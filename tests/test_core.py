import unittest
from penta_lemon.core import Lemon, Const, Xxxv

class TestCore(unittest.TestCase):

    def setUp(self):
        self.lemon = Lemon()
        self.lemon_list = []
        self.lemon_list.append(Lemon())

    def test_lemon(self):
        for i in range(5): #前五爻
            self.lemon.feedXxxv(Xxxv(Const.XxxvCode.OLD_BDEM))
            self.assertIsNone(self.lemon.octaNopoPentaMiri)
        self.lemon.feedXxxv(Xxxv(Const.XxxvCode.OLD_BDEM)) #第六爻
        self.assertIsNotNone(self.lemon.octaNopoPentaMiri.pentaMiriCode)
        self.assertIsNotNone(self.lemon.octaNopoPentaMiri.octaNopoCode)
        self.lemon.feedXxxv(Xxxv(Const.XxxvCode.OLD_BDEM)) #第六+1爻(重置)
        self.assertIsNone(self.lemon.octaNopoPentaMiri)

    def test_lemon_list(self):
        for i in range(6):
            self.lemon_list[0].feedXxxv(Xxxv(Const.XxxvCode.OLD_BDEM))
        self.assertIsNotNone(self.lemon_list[0].octaNopoPentaMiri.pentaMiriCode)
        self.assertIsNotNone(self.lemon_list[0].octaNopoPentaMiri.octaNopoCode)
        self.lemon_list.append(Lemon())
        self.lemon_list[1].feedXxxv(self.lemon_list[0].octaNopoPentaMiri.completedYypToXvvv())
        self.assertIsNotNone(self.lemon_list[1].yyp.sixXxxv[0])

if __name__ == "__main__":
    unittest.main()
