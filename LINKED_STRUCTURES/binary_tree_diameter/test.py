from LINKED_STRUCTURES.binary_tree_diameter.app import diameterOfBinaryTree
from utils import compose_binary_tree


def test_case_1():
    t = [1,2,3,4,5]
    bt = compose_binary_tree(t)
    assert diameterOfBinaryTree(bt) == 3