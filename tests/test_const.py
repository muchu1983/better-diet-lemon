import unittest
import random
from penta_lemon.const import Const

class TestConst(unittest.TestCase):

    def setUp(self):
        pass

    def test_const(self):
        self.assertEqual(len(Const.YypCode), 64+8)
        self.assertEqual(Const.YypCode._121212.value[2], Const.YypCode.火.value + Const.YypCode.水.value)

    def test_yyp_code_map(self):
        self.assertEqual(len(Const.YypCodeMap), 64)
        yyp_code_key = "".join(random.choice("12") for _ in range(6))
        self.assertEqual(Const.YypCodeMap[yyp_code_key].value[0], yyp_code_key)
        self.assertIsNotNone(Const.YypCodeMap[yyp_code_key].value[1])
        self.assertIsNotNone(Const.YypCodeMap[yyp_code_key].value[2])
        
if __name__ == "__main__":
    unittest.main()