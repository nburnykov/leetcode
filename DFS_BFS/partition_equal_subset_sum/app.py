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


def canPartition2(nums: List[int]) -> bool:
    # sliding window doesn't work here, because there could be gaps in sequences that produce the right sum
    sorted_nums = sorted(nums)
    if sum(sorted_nums) % 2 != 0:
        return False

    target_sum = sum(sorted_nums) // 2
    l, r = 0, 0
    s = 0
    while r < len(sorted_nums) and l < len(sorted_nums):
        if s == target_sum:
            return True
        if s > target_sum:
            s -= sorted_nums[l]
            l += 1
        else:
            s += sorted_nums[r]
            r += 1

    return False

