from LINKED_STRUCTURES.balanced_binary_tree.app import isBalanced
from utils import compose_binary_tree


def test_case_1():
    t = [3, 9, 20, None, None, 7]
    bt = compose_binary_tree(t)
    assert isBalanced(bt)


def test_case_2():
    t = [1,2,2,3,None,None,3,4,None,None,4]
    bt = compose_binary_tree(t)
    assert not isBalanced(bt)


def test_case_3():
    t = [1,None,2,None, None, None,3]
    bt = compose_binary_tree(t)
    assert not isBalanced(bt)