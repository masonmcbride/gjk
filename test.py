import unittest
from gjk import *

class Testgjk(unittest.TestCase):

    def test_true(self):
        s1 = Shape([Point(4,11), Point(4,5), Point(9,9)])
        s2 = Shape([Point(5,7), Point(7,3), Point(10,2), Point(12, 7)])

        self.assertTrue(GJK(s1, s2))

    def test_false(self):
        s1 = Shape([Point(4,11), Point(4,5), Point(9,9)])
        s2 = Shape([Point(8,5), Point(7,3), Point(10,2), Point(12, 7)])
        self.assertFalse(GJK(s1, s2))

    def test_negative_true(self):
        s1 = Shape([Point(4,11), Point(4,5), Point(9,9)])
        s2 = Shape([Point(8,5), Point(-2, 4), Point(2, 8)])

        self.assertTrue(GJK(s1, s2))

    def test_negative_false(self):
        s1 = Shape([Point(-4,11), Point(-4,5), Point(-9,9)])
        s2 = Shape([Point(8,-5), Point(-2, -4), Point(2, -8)])

        self.assertFalse(GJK(s1, s2))

if __name__ == '__main__':
    unittest.main()
