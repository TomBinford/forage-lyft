import unittest
from datetime import datetime
from battery import *


class TestBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        future = today.replace(year=today.year + 2, day=today.day + 1)
        spindler = SpindlerBattery(today, future)
        print(spindler.should_be_serviced())
        self.assertTrue(spindler.should_be_serviced())

    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        future = today.replace(year=today.year + 1)
        spindler = SpindlerBattery(today, future)
        self.assertFalse(spindler.should_be_serviced())

    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        future = today.replace(year=today.year + 4, day=today.day + 1)
        nubbin = NubbinBattery(today, future)
        self.assertTrue(nubbin.should_be_serviced())

    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today().date()
        future = today.replace(year=today.year + 3)
        nubbin = NubbinBattery(today, future)
        self.assertFalse(nubbin.should_be_serviced())


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.makeSuite(TestBattery))
