###########################################################################################
# leetcode problem https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
###########################################################################################

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    head = root
    while root is not None and root.left is not None:  # not a leaf node
        root_next = root.left
        while root:
            root.left.next = root.right  # link between child nodes
            if root.next:  # right root exists
                root.right.next = root.next.left
            root = root.next  # moving horizontally
        root = root_next  # one step down the tree
    return head