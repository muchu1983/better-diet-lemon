import unittest
from lemon64.const import XxxvCode, OctaNopoCode
from lemon64.core import Xxxv
from lemon64.lemon import Lemon

class TestLemon(unittest.TestCase):

    def setUp(self):
        self.lemon = Lemon()
        self.lemon_list = []
        self.lemon_list.append(Lemon())

    def test_lemon(self):
        for i in range(5): #前五爻
            self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
            self.assertIsNone(self.lemon.octaNopoPentaMiri.yyp)
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM)) #第六爻
        self.assertIsNotNone(self.lemon.octaNopoPentaMiri.pentaMiriCode)
        self.assertIsNotNone(self.lemon.octaNopoPentaMiri.octaNopoCode)
        self.assertIsNotNone(self.lemon.octaNopoPentaMiri.completedYypToXvvv())
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM)) #第六+1爻(重置)
        self.assertIsNone(self.lemon.octaNopoPentaMiri.yyp)

    def test_lemon_list(self):
        for i in range(6):
            self.lemon_list[0].feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
        self.assertIsNotNone(self.lemon_list[0].octaNopoPentaMiri.pentaMiriCode)
        self.assertIsNotNone(self.lemon_list[0].octaNopoPentaMiri.octaNopoCode)
        self.lemon_list.append(Lemon())
        self.lemon_list[1].feedXxxv(self.lemon_list[0].octaNopoPentaMiri.completedYypToXvvv())
        self.assertIsNotNone(self.lemon_list[1].yyp.sixXxxv[0])

    def test_getCarryXxxv(self):
        for i in range(5):
            self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BAYT))
            self.assertIsNone(self.lemon.getCarryXxxv())
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BAYT))
        self.assertIsNotNone(self.lemon.getCarryXxxv())
        self.assertEqual(self.lemon.octaNopoPentaMiri.octaNopoCode, OctaNopoCode.EARTH)
        self.assertEqual(self.lemon.getCarryXxxv().xxxvCode, XxxvCode.OLD_BAYT)

if __name__ == "__main__":
    unittest.main()
