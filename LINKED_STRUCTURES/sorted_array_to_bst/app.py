# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from collections import deque
from typing import List, Optional

from utils import TreeNode


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    root = None
    q = [(root, 0, len(nums) - 1)]

    while len(q) > 0:
        root_node, l, r = q.pop(-1)

        if r < l:
            continue

        mid = (l + r) // 2
        node = TreeNode()
        node.val = nums[mid]

        if root_node is None:
            root = node
        else:
            if root_node.val > node.val:
                root_node.left = node
            else:
                root_node.right = node

        q.append((node, mid + 1, r))
        q.append((node, l, mid - 1))

    return root
