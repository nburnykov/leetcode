from LINKED_STRUCTURES.same_tree.app import isSameTree
from utils import compose_binary_tree


def test_case_1():
    p = [1, 2, 3]
    q = [1, 2, 3]
    pt = compose_binary_tree(p)
    qt = compose_binary_tree(q)
    assert isSameTree(pt, qt)


def test_case_2():
    p = [1, 2]
    q = [1, 2, 3]
    pt = compose_binary_tree(p)
    qt = compose_binary_tree(q)
    assert not isSameTree(pt, qt)