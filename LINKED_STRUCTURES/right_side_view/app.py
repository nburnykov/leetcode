# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import List, Optional

from utils import TreeNode


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    """
    level order traversal, the right non-none node wins
    """
    level_nodes = [root]
    result = []
    while any(level_nodes):
        for i in range(len(level_nodes) -1, -1, -1):
            if level_nodes[i] is not None:
                result.append(level_nodes[i].val)
                break
        level_nodes_next = []
        for node in level_nodes:
            if node is not None:
                level_nodes_next.extend([node.left, node.right])
        level_nodes = level_nodes_next
    return result
