###########################################################################################
# leetcode problem https://leetcode.com/problems/balanced-binary-tree/
###########################################################################################
from collections import deque
from typing import Optional

from utils import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    heights = {}
    seen = set()
    q = [root]
    while len(q) > 0:
        node = q[-1]
        node_id = id(node)
        seen.add(node_id)

        if node is None:
            q.pop(-1)
            continue

        r_node_id, l_node_id = id(node.right), id(node.left)

        if l_node_id not in seen:
            q.append(node.left)
            continue
        if r_node_id not in seen:
            q.append(node.right)
            continue

        max_l = heights.pop(l_node_id, 0)
        max_r = heights.pop(r_node_id, 0)

        if abs(max_l - max_r) > 1:
            return False
        heights[node_id] = max(max_r, max_l) + 1
        q.pop(-1)

    return True