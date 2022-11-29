import unittest
from engine import *


class TestEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        capulet = CapuletEngine(0, 30000 + 1)
        self.assertTrue(capulet.should_be_serviced())

    def test_capulet_should_not_be_serviced(self):
        capulet = CapuletEngine(30000, 50000)
        self.assertFalse(capulet.should_be_serviced())

    def test_sternman_should_be_serviced(self):
        sternman = SternmanEngine(True)
        self.assertTrue(sternman.should_be_serviced())

    def test_sternman_should_not_be_serviced(self):
        sternman = SternmanEngine(False)
        self.assertFalse(sternman.should_be_serviced())

    def test_willoughby_should_be_serviced(self):
        willoughby = WilloughbyEngine(0, 60000 + 1)
        self.assertTrue(willoughby.should_be_serviced())

    def test_willoughby_should_not_be_serviced(self):
        willoughby = WilloughbyEngine(100000, 135000)
        self.assertFalse(willoughby.should_be_serviced())


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.makeSuite(TestEngine))
