###########################################################################################
# leetcode problem https://leetcode.com/problems/house-robber/
###########################################################################################

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) < 3:
        return max(nums)

    nums.insert(0, 0)
    for i in range(2, len(nums)):
        nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])

    return nums[-1]
