import unittest
import random
from penta_lemon.const import YypCode, YypCodeMap, EmojiMap

class TestConst(unittest.TestCase):

    def setUp(self):
        pass

    def test_const(self):
        self.assertEqual(len(YypCode), 64+8)
        self.assertEqual(YypCode._121212.value[4], YypCode.火.value + YypCode.水.value)

    def test_yyp_code_map(self):
        self.assertEqual(len(YypCodeMap), 64)
        yyp_code_key = "".join(random.choice("12") for _ in range(6))
        self.assertEqual(YypCodeMap[yyp_code_key].value[0], yyp_code_key)
        self.assertIsNotNone(YypCodeMap[yyp_code_key].value[1])
        self.assertIsNotNone(YypCodeMap[yyp_code_key].value[2])
        self.assertIsNotNone(YypCodeMap[yyp_code_key].value[3])
        self.assertIsNotNone(YypCodeMap[yyp_code_key].value[4])
        
    def testEmojiMap(self):
        for key in EmojiMap:
            pass
            #print(EmojiMap[key])

if __name__ == "__main__":
    unittest.main()