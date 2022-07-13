###########################################################################################
# leetcode problem  https://leetcode.com/problems/binary-tree-level-order-traversal/
###########################################################################################
from typing import Optional, List

from utils import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    nxt_lvl = [root]
    result = []
    while len(nxt_lvl) > 0:
        val = []
        nxt = []
        for n in nxt_lvl:
            val.append(n.val)
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        result.append(val)
        nxt_lvl = nxt.copy()
    return result