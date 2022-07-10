###########################################################################################
# leetcode problem  https://leetcode.com/problems/first-missing-positive/
###########################################################################################
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    """
    Main idea here is that in ideal case nums must contain all the numbers from 1 to len(nums) otherwise there will be
    gaps that contain numbers < 0 or > len(nums)
    First we need to clean up all the values outside this array range, next place valid ones on their respective places
    First non-increasing gap will be the answer
    """

    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] > len(nums):
            nums[i] = 0

    nums.append(0)

    for i in range(len(nums)):
        while nums[i] not in {i, 0}:  # swap
            a = nums[i]
            b = nums[nums[i]]
            if a == b:
                b = 0
            nums[i] = b
            nums[a] = a

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)

