###########################################################################################
# leetcode problem https://leetcode.com/problems/balanced-binary-tree/
###########################################################################################
from collections import deque
from typing import Optional

from utils import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    def isSubBalanced(root: TreeNode) -> bool:
        max_depth_left, max_depth_right = 0, 0
        q = deque([(1, root.left, False), (1, root.right, True)])
        while len(q) > 0:
            current_depth, item, is_right = q.popleft()

            if is_right:
                max_depth_right = max(max_depth_right, current_depth)
            else:
                max_depth_left = max(max_depth_left, current_depth)

            if item is not None:
                q.append((current_depth + 1, item.left, is_right))
                q.append((current_depth + 1, item.right, is_right))
        return abs(max_depth_right - max_depth_left) < 2

    q = deque([root])
    while len(q) > 0:
        item = q.popleft()
        if item is None:
            continue
        if not isSubBalanced(item):
            return False
        else:
            q.append(item.left)
            q.append(item.right)

    return True
