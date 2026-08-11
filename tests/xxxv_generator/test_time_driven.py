import unittest
from lemon64.core import Xxxv
from lemon64.xxxv_generator.time_driven import TimeDrivenXxxvGen

class TestTimeDrivenXxxvGen(unittest.TestCase):

    def setUp(self):
        self.tdxg = TimeDrivenXxxvGen()

    def test_time_driven_xxxv_generator(self):
        self.assertIsInstance(self.tdxg.getXxxv(), Xxxv)


if __name__ == "__main__":
    unittest.main()
