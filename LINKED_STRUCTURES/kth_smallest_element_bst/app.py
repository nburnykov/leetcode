# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from collections import deque
from heapq import heappush, heappop
from typing import Optional

from utils import TreeNode


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    q = [root]
    while True:
        while root is not None:
            q.append(root)
            root = root.left
        root = q.pop(-1)
        k -= 1
        if k == 0:
            return root.val

        root = root.right
