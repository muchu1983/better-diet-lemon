import unittest
from lemon64.const import XxxvCode, OctaNopoCode
from lemon64.core import Xxxv
from lemon64.lemon import Lemon

class TestOnpm(unittest.TestCase):

    def setUp(self):
        self.lemon = Lemon()

    def test_onpm(self):
        #喂食水火既济 121212
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BAYT))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BAYT))
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BAYT))
        self.assertEqual(self.lemon.octaNopoPentaMiri.findYypId(), "121212")
        self.assertEqual(self.lemon.octaNopoPentaMiri.octaNopoCode, OctaNopoCode.WATER)
        self.assertEqual(self.lemon.octaNopoPentaMiri.completedYypToXvvv().xxxvCode, XxxvCode.YOUNG_BDEM)
        #喂食地天泰 111222
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BDEM))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BAYT))
        self.lemon.feedXxxv(Xxxv(XxxvCode.OLD_BAYT))
        self.lemon.feedXxxv(Xxxv(XxxvCode.YOUNG_BAYT))
        self.assertEqual(self.lemon.octaNopoPentaMiri.findYypId(), "111222")
        self.assertEqual(self.lemon.octaNopoPentaMiri.octaNopoCode, OctaNopoCode.EARTH)
        self.assertEqual(self.lemon.octaNopoPentaMiri.completedYypToXvvv().xxxvCode, XxxvCode.OLD_BAYT)

if __name__ == "__main__":
    unittest.main()
