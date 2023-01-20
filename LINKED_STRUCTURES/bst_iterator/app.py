# https://leetcode.com/problems/binary-search-tree-iterator
from typing import Optional

from utils import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.s = []
        if root is not None:
            self.go_left(root)

    def go_left(self, node: TreeNode):
        while node is not None:
            self.s.append(node)
            node = node.left

    def next(self) -> int:
        node = self.s.pop(-1)
        if node.right is not None:
            self.go_left(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.s) > 0
