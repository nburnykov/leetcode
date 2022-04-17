###########################################################################################
# leetcode problem  https://leetcode.com/problems/subtree-of-another-tree/
###########################################################################################

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare_trees(root: TreeNode, subroot: TreeNode) -> bool:
    q = [(root, subroot)]
    seen = set()
    while len(q) > 0:
        r, sr = q.pop(-1)
        if not r.val == sr.val:
            return False

        l_tpl = r.left, sr.left
        if l_tpl[0] and l_tpl[1] and l_tpl not in seen:
            q.append(l_tpl)
            seen.add(l_tpl)

        if (l_tpl[0] is None) != (l_tpl[1] is None):
            return False

        r_tpl = r.right, sr.right
        if r_tpl[0] and r_tpl[1] and r_tpl not in seen:
            q.append(r_tpl)
            seen.add(r_tpl)

        if (r_tpl[0] is None) != (r_tpl[1] is None):
            return False
    return True


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:  # O(1) space solution
    if not root or not subRoot:  # corner cases
        return False

    q = [root]
    seen = set()
    while len(q) > 0:
        node = q.pop(-1)
        if node.val == subRoot.val:
            r = compare_trees(node, subRoot)
            if r:
                return True
        if node.left and node.left not in seen:
            seen.add(node.left)
            q.append(node.left)
        if node.right and node.right not in seen:
            seen.add(node.right)
            q.append(node.right)

    return False
