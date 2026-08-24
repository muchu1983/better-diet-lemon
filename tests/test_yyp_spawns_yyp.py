import unittest
from lemon64.yyp_spawns_yyp import run_yyp_spawns_yyp

class TestYypSpawnsYyp(unittest.TestCase):

    def setUp(self):
        pass

    def test_yyp_spawns_yyp(self):
        with self.assertRaises(SystemExit) as ctx:
            run_yyp_spawns_yyp()
        self.assertEqual(ctx.exception.code, 0)

if __name__ == "__main__":
    unittest.main()