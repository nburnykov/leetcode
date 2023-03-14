from typing import Optional, List

from utils import TreeNode


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if root is None:
        return []

    result = []
    q = [(root, 0, [])]
    while len(q) > 0:
        node, path_sum, components = q.pop()
        if node is None:
            continue

        components.append(node.val)
        path_sum += node.val
        is_leaf = (node.left and node.right) is None
        if path_sum == targetSum and is_leaf:
            result.append(components)

        q.append((node.left, path_sum, components.copy()))
        q.append((node.right, path_sum, components.copy()))

    return result