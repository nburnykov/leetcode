import unittest

from DFS_BFS.combination_sum_iii.app import combinationSum3


class TestApp(unittest.TestCase):
    def test_case_1(self):
        k = 3
        n = 7
        r = [[1, 2, 4]]
        self.assertEqual(combinationSum3(k, n), r)

    def test_case_2(self):
        k = 3
        n = 9
        r = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        self.assertEqual(sorted(combinationSum3(k, n), key=lambda x: x[0]), r)

    def test_case_3(self):
        k = 4
        n = 1
        r = []
        self.assertEqual(combinationSum3(k, n), r)
