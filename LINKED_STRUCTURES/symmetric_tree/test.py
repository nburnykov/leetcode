from LINKED_STRUCTURES.symmetric_tree.app import isSymmetric
from utils import compose_binary_tree


def test_case_1():
    t = [1, 2, 2, 3, 4, 4, 3]
    tt = compose_binary_tree(t)
    assert isSymmetric(tt)