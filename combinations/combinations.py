###########################################################################################
# leetcode problem https://leetcode.com/problems/combinations/
###########################################################################################

from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    x = 1
    result = []
    stack = []
    last_value = list(range(n - k + 1, n + 1))
    while True:
        if len(stack) < k and x <= n:
            stack.append(x)
            x += 1
        else:
            if stack == last_value:  # early stopping
                return result
            x = stack.pop() + 1

        if len(stack) == k:
            result.append(stack[:])
