###########################################################################################
# leetcode problem https://leetcode.com/problems/path-sum-iii/
###########################################################################################
from typing import Optional, List

from utils import TreeNode


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    if root is None:
        return 0

    stack = [(root, 0)]
    count = 0
    sum_cache = {0: 1}
    seen = set()
    while len(stack) > 0:
        node, path_sum = stack[-1]

        path_sum += node.val

        if id(node) not in seen:
            seen.add(id(node))

            count += sum_cache.get(path_sum - targetSum, 0)
            sum_cache[path_sum] = sum_cache.get(path_sum, 0) + 1

        if node.right is not None and id(node.right) not in seen:
            stack.append((node.right, path_sum))
            continue
        if node.left is not None and id(node.left) not in seen:
            stack.append((node.left, path_sum))
            continue

        sum_cache[path_sum] -= 1
        stack.pop(-1)

    return count

