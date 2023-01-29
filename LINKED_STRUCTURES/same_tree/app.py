# https://leetcode.com/problems/same-tree/
from typing import Optional

from utils import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    q = [(p, q)]

    while len(q) > 0:
        n1, n2 = q.pop(-1)

        if bool(n1) != bool(n2):  # xor
            return False
        if (n1 and n2) is None:
            continue
        if n1.val != n2.val:
            return False

        q.append((n1.left, n2.left))
        q.append((n1.right, n2.right))

    return True
