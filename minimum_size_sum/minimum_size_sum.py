###########################################################################################
# leetcode problem https://leetcode.com/problems/minimum-size-subarray-sum/
###########################################################################################

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    p2, s = 0, 0
    min_len = float('inf')
    for p1 in range(len(nums)):
        s += nums[p1]
        while s >= target and p2 <= p1:
            min_len = min(min_len, p1 - p2 + 1)
            s -= nums[p2]
            p2 += 1
    return min_len if min_len != float('inf') else 0


