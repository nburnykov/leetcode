# https://leetcode.com/problems/partition-equal-subset-sum
from collections import deque
from typing import List


def canPartition(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False

    t = s / 2
    indexes = set(range(len(nums)))
    q = deque([({0}, nums[0])])
    visited = set()
    while len(q) > 0:
        sub_indexes, sub_sum = q.popleft()
        if sub_sum == t:
            return True
        for i in indexes - sub_indexes:
            s = sub_sum + nums[i]
            if s == t:
                return True
            if s < t:
                if s not in visited:
                    q.append((sub_indexes | {i}, s))
                    visited.add(s)

    return False

