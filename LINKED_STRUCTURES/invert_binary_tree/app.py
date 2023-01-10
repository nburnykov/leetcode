###########################################################################################
# leetcode problem https://leetcode.com/problems/invert-binary-tree/
###########################################################################################
from collections import deque
from typing import Optional

from utils import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    q = deque([root])
    while len(q) > 0:
        item = q.popleft()
        if item is not None:
            item.left, item.right = item.right, item.left
            q.append(item.left)
            q.append(item.right)
    return root