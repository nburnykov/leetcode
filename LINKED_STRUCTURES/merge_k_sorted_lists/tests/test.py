import unittest

from LINKED_STRUCTURES.merge_k_sorted_lists.app import mergeKLists
from utils import create_linked_list, read_linked_list

class TestApp(unittest.TestCase):
    def test_case_1(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        r = [1, 1, 2, 3, 4, 4, 5, 6]
        lli = [create_linked_list(l) for l in lists]
        self.assertEqual(read_linked_list(mergeKLists(lli)), r)
