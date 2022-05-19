from DFS_BFS.target_copy.app import getTargetCopy
from utils import compose_binary_tree, TreeNode


def test_case_1():
    tree = [7, 4, 3, None, None, 6, 19]
    target = 3
    l_tree = compose_binary_tree(tree)
    l_clone = compose_binary_tree(tree)
    tn = TreeNode(val=target)
    result_node = getTargetCopy(l_tree, l_clone, tn)
    assert result_node.val == tn.val


def test_case_2():
    tree = [7]
    target = 7
    l_tree = compose_binary_tree(tree)
    l_clone = compose_binary_tree(tree)
    tn = TreeNode(val=target)
    result_node = getTargetCopy(l_tree, l_clone, tn)
    assert result_node.val == tn.val


def test_case_3():
    tree = [8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]
    target = 4
    l_tree = compose_binary_tree(tree)
    l_clone = compose_binary_tree(tree)
    tn = TreeNode(val=target)
    result_node = getTargetCopy(l_tree, l_clone, tn)
    assert result_node.val == tn.val
