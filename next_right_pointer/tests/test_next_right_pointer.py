from next_right_pointer.binary_tree_array import compose_binary_tree
from next_right_pointer.next_right_pointer import connect


def test_case_1():
    root = [1, 2, 3, 4, 5, 6, 7]
    nodes = compose_binary_tree(root)
    result = connect(nodes)
    pass