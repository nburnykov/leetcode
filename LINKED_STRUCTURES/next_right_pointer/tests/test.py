from utils import compose_binary_tree, decompose_binary_tree
from LINKED_STRUCTURES.next_right_pointer.app import connect


def test_case_1():
    root = [1, 2, 3, 4, 5, 6, 7]
    nodes = compose_binary_tree(root)
    result = connect(nodes)
    print(decompose_binary_tree(result))