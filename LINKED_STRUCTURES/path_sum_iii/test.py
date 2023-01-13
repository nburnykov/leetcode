from LINKED_STRUCTURES.path_sum_iii.app import pathSum
from utils import compose_binary_tree


def test_case_1():
    t = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    bt = compose_binary_tree(t)
    assert pathSum(bt, 22) == 3


def test_case_2():
    t = [5, 5, 5]
    bt = compose_binary_tree(t)
    assert pathSum(bt, 10) == 2


def test_case_3():
    t = [1, 2, 2, 3, 4, 3 ,6]
    bt = compose_binary_tree(t)
    assert pathSum(bt, 5) == 2
