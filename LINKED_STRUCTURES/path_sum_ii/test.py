from LINKED_STRUCTURES.path_sum_ii.app import pathSum
from utils import compose_binary_tree


def test_case_1():
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    bt = compose_binary_tree(root)
    targetSum = 22
    result = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert pathSum(bt, targetSum) == result
