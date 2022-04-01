###########################################################################################
# leetcode problem https://leetcode.com/problems/merge-two-binary-trees/
###########################################################################################

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
        return
    if bool(root1) != bool(root2):  # XOR - one of the roots is None, but not both
        return root1 or root2

    head = TreeNode()
    node_stack = [(root1, root2)]
    result_stack = [head]

    while len(node_stack) > 0:
        current1, current2 = node_stack.pop(-1)
        result = result_stack.pop(-1)

        result.val = current1.val + current2.val
        if current1.left and current2.left:
            new_node = TreeNode()
            result.left = new_node
            
            node_stack.append((current1.left, current2.left))
            result_stack.append(new_node)
        else:
            result.left = current1.left or current2.left

        if current1.right and current2.right:
            new_node = TreeNode()
            result.right = new_node

            node_stack.append((current1.right, current2.right))
            result_stack.append(new_node)
        else:
            result.right = current1.right or current2.right

    return head
