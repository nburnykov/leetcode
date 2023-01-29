# https://leetcode.com/problems/symmetric-tree/
from typing import Optional

from utils import TreeNode


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    Level order traversal
    """
    if root is None:
        return True
    level_nodes = [root.left, root.right]
    while any(level_nodes):
        for i in range(len(level_nodes) // 2):
            left, right = level_nodes[i], level_nodes[-i - 1]
            if bool(left) != bool(right):
                return False
            if left is not None and left.val != right.val:
                return False

        level_nodes_next = []
        for ln in level_nodes:
            if ln is not None:
                level_nodes_next.extend([ln.left, ln.right])
        level_nodes = level_nodes_next

    return True
