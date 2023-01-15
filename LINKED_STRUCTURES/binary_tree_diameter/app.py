###########################################################################################
# leetcode problem https://leetcode.com/problems/diameter-of-binary-tree
###########################################################################################

from collections import deque
from typing import Optional, Dict

from utils import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    diameters: Dict[str, int] = {}
    seen = set()
    max_diameter = 0
    q = [(root, "root", "L")]
    while len(q) > 0:
        node, parent_id, prefix = q[-1]
        node_id = id(node)
        seen.add(node_id)
        if node.left is not None and id(node.left) not in seen:
            q.append((node.left, node_id, "L"))
            continue
        if node.right is not None and id(node.right) not in seen:
            q.append((node.right, node_id, "R"))
            continue
        l_d = diameters.pop(f"L_{node_id}", 0)
        r_d = diameters.pop(f"R_{node_id}", 0)
        max_diameter = max(max_diameter, l_d + r_d)
        diameters[f"{prefix}_{parent_id}"] = max(l_d, r_d) + 1
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
