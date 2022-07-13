from LINKED_STRUCTURES.level_order_traversial.app import levelOrder
from utils import compose_binary_tree, decompose_binary_tree


def test_case_1():
    root = [3, 9, 20, None, None, 15, 7]
    r = [[3], [9, 20], [15, 7]]
    tr = compose_binary_tree(root)
    assert levelOrder(tr) == r

def test_case_2():
    root = [1]
    r = [[1]]
    tr = compose_binary_tree(root)
    assert levelOrder(tr) == r