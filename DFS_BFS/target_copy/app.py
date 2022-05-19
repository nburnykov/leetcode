###########################################################################################
# leetcode problem https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
###########################################################################################

from collections import deque

from utils import TreeNode


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    q = deque([(original, [])])
    result = []
    while len(q) > 0:  # BFS
        node, path = q.popleft()
        if node.val == target.val:
            result = path
            break

        if node.left:
            p = path.copy()
            p.append('L')
            q.append((node.left, p))

        if node.right:
            p = path.copy()
            p.append('R')
            q.append((node.right, p))

    c = cloned
    for direction in result:  # follow the path
        if direction == 'L':
            c = c.left
        else:
            c = c.right

    return c