###########################################################################################
# leetcode problem https://leetcode.com/problems/diameter-of-binary-tree
###########################################################################################

from collections import deque
from typing import Optional, Dict

from utils import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    diameters: Dict[int, int] = {id(None): 0}
    max_diameter = 0
    q = [root]
    while len(q) > 0:
        node = q[-1]
        if id(node.left) not in diameters:
            q.append(node.left)
            continue
        if id(node.right) not in diameters:
            q.append(node.right)
            continue
        l_d = diameters.pop(id(node.left)) if node.left is not None else 0
        r_d = diameters.pop(id(node.right)) if node.right is not None else 0
        max_diameter = max(max_diameter, l_d + r_d)
        diameters[id(node)] = max(l_d, r_d) + 1
        q.pop(-1)
    return max_diameter



def diameterOfBinaryTreeRecursive(root: Optional[TreeNode]) -> int:
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
