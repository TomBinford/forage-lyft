import unittest
from tires import *


class TestTires(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        carrigan = CarriganTires((0.9, 0, 0, 0))
        self.assertTrue(carrigan.should_be_serviced())

    def test_carrigan_should_not_be_serviced(self):
        carrigan = CarriganTires((0.8, 0.8, 0.8, 0.8))
        self.assertFalse(carrigan.should_be_serviced())

    def test_octoprime_should_be_serviced(self):
        octoprime = OctoprimeTires((0.8, 0.8, 0.8, 0.8))
        self.assertTrue(octoprime.should_be_serviced())

    def test_octoprime_should_not_be_serviced(self):
        octoprime = OctoprimeTires((0.9, 0, 0, 0))
        self.assertFalse(octoprime.should_be_serviced())


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.makeSuite(TestTires))
