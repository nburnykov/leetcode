from LINKED_STRUCTURES.next_right_pointer_2.app import connect
from utils import compose_binary_tree


def test_case_1():
    root = [1, 2, 3, 4, 5, None, 7]
    nodes = compose_binary_tree(root)
    result = connect(nodes)
    pass
