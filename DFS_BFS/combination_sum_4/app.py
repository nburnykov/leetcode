###########################################################################################
# leetcode problem  https://leetcode.com/problems/combination-sum-iv/
###########################################################################################
from collections import deque
from typing import List


def combinationSum4_slow(nums: List[int], target: int) -> int:
    """
    slow and painful bfs implementation
    """
    q = deque([([n], target - n) for n in nums])
    result = 0
    while len(q) > 0:  # bfs
        terms, balance = q.popleft()

        if balance < 0:
            continue

        if balance == 0:
            result += 1
            continue

        for n in nums:
            q.append((terms + [n], balance - n))

    return result


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for n in nums:
            shift = i - n
            if shift >= 0:
                dp[i] += dp[shift]
    return dp[-1]


def combinationSum4_opt(nums: List[int], target: int) -> int:
    """
    A try to optimize solution by memory
    """

    dp = deque([1])
    mn = max(nums)
    for i in range(1, target + 1):
        dp.append(0)
        for n in nums:

            if n < len(dp):
                dp[-1] += dp[-n - 1]

            if len(dp) > mn + 1:
                dp.popleft()

    return dp.pop()
