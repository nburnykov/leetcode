###########################################################################################
# leetcode problem https://leetcode.com/problems/deepest-leaves-sum/
###########################################################################################

from typing import Optional
from utils import TreeNode


def deepestLeavesSum(root: Optional[TreeNode]) -> int:

    node_array = [root] if root else []
    current_sum = 0
    while len(node_array) > 0:
        current_sum = 0
        new_node_array = []
        for n in node_array:
            current_sum += n.val
            if n.left:
                new_node_array.append(n.left)
            if n.right:
                new_node_array.append(n.right)
        node_array = new_node_array

    return current_sum