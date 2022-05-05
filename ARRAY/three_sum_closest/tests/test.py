import unittest

from ARRAY.three_sum_closest.app import threeSumClosest


class TestApp(unittest.TestCase):
    def test_case_1(self):
        n = [-1, 2, 1, -4]
        t = 1
        r = 2
        self.assertEqual(threeSumClosest(n, t), r)

    def test_case_2(self):
        n = [0, 0, 0]
        t = 1
        r = 0
        self.assertEqual(threeSumClosest(n, t), r)

    def test_case_3(self):
        n = [1, 1, 1, 0]
        t = -100
        r = 2
        self.assertEqual(threeSumClosest(n, t), r)
