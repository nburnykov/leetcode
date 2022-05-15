from LINKED_STRUCTURES.deepest_leaves_sum.app import deepestLeavesSum
from utils import compose_binary_tree


def test_case_1():
    tree = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    r = 15
    tree = compose_binary_tree(tree)
    assert deepestLeavesSum(tree) == r