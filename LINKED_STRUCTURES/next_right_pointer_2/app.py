###########################################################################################
# leetcode problem https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
###########################################################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


def connect(root: 'Node') -> 'Node':  # O(1) space solution without recursion
    if not root:  # corner cases
        return

    node = root
    node_start = None
    node_current = None
    while True:
        if node.left:
            if not node_start:
                node_start = node.left
                node_current = node.left
            else:
                node_current.next = node.left
                node_current = node.left

        if node.right:
            if not node_start:
                node_start = node.right
                node_current = node.right
            else:
                node_current.next = node.right
                node_current = node.right

        node = node.next
        if not node:
            if not node_start:
                return root
            else:
                node = node_start
                node_start = None
