from LINKED_STRUCTURES.subtree_of_another_tree.app import isSubtree
from utils import compose_binary_tree


def test_case_1():
    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]
    r = compose_binary_tree(root)
    sr = compose_binary_tree(subRoot)
    assert isSubtree(r, sr)


def test_case_2():
    root = [3, 4, 5, 1, 2, None, None, None, None, 0]
    subRoot = [4, 1, 2]
    r = compose_binary_tree(root)
    sr = compose_binary_tree(subRoot)
    assert not isSubtree(r, sr)
