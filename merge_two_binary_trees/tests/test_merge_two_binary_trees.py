from next_right_pointer.binary_tree_array import compose_binary_tree, decompose_binary_tree
from merge_two_binary_trees.merge_two_binary_trees import mergeTrees


def test_compose_decompose_1():
    input = [0, 1, 2, 3, 4, 5, 6]
    bt = compose_binary_tree(input)
    assert decompose_binary_tree(bt) == input

def test_compose_decompose_2():
    input = [0, 1, 2, 3, 4, 5]
    bt = compose_binary_tree(input)
    assert decompose_binary_tree(bt) == input

def test_compose_decompose_3():
    input = [0, 1, 2, None, None, 5]
    bt = compose_binary_tree(input)
    assert decompose_binary_tree(bt) == input


def test_case_1():
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]
    output = [3, 4, 5, 5, 4, None, 7]
    t1 = compose_binary_tree(root1)
    t2 = compose_binary_tree(root2)
    mt = mergeTrees(t1, t2)
    assert decompose_binary_tree(mt) == output

def test_case_2():
    root1 = [1]
    root2 = [1, 2]
    output = [2, 2]
    t1 = compose_binary_tree(root1)
    t2 = compose_binary_tree(root2)
    mt = mergeTrees(t1, t2)
    assert decompose_binary_tree(mt) == output


def test_case_3():
    root1 = []
    root2 = [1]
    output = [1]
    t1 = compose_binary_tree(root1)
    t2 = compose_binary_tree(root2)
    mt = mergeTrees(t1, t2)
    assert decompose_binary_tree(mt) == output
