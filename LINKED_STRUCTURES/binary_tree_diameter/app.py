###########################################################################################
# leetcode problem https://leetcode.com/problems/diameter-of-binary-tree
###########################################################################################

from collections import deque
from typing import Optional

from utils import TreeNode


def diameterOfBinaryTreeIterative(root: Optional[TreeNode]) -> int:
    def subDiameter(sub_root: TreeNode) -> int:
        max_l, max_r = 0, 0
        q = deque([(1, sub_root.right, True), (1, sub_root.left, False)])
        while len(q) > 0:
            depth, node, is_right = q.popleft()
            if node is None:
                continue
            if is_right:
                max_r = max(max_r, depth)
            else:
                max_l = max(max_l, depth)
            q.append((depth + 1, node.left, is_right))
            q.append((depth + 1, node.right, is_right))

        return max_l + max_r

    q = deque([root])
    diameter = 0
    while len(q) > 0:
        node = q.popleft()
        if node is None:
            continue
        depth = subDiameter(node)
        diameter = max(diameter, depth)
        q.append(node.left)
        q.append(node.right)

    return diameter


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    best = 0

    def diameter(sub_root: Optional[TreeNode]) -> int:
        nonlocal best
        if sub_root is None:
            return 0
        r_d = diameter(sub_root.right)
        l_d = diameter(sub_root.left)
        best = max(best, r_d + l_d)
        return max(l_d, r_d) + 1

    diameter(root)

    return best
