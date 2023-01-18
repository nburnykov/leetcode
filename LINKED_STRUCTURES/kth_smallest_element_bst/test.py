from LINKED_STRUCTURES.kth_smallest_element_bst.app import kthSmallest
from utils import compose_binary_tree


def test_case_1():
    t = [3,1,4,None,2]
    bt = compose_binary_tree(t)
    k = 1
    assert kthSmallest(bt, k) == 1