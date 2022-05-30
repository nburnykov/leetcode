###########################################################################################
# leetcode problem https://leetcode.com/problems/next-permutation/
###########################################################################################

# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return

    a, b = None, None
    for i in range(len(nums) - 2, -1, -1):  # finding the pivot
        if nums[i+1] > nums[i]:
            a = i
            break

    if a is not None:
        for j in range(len(nums) - 1, a, -1):  # finding the rightmost successor
            if nums[j] > nums[a]:
                b = j
                break

    if a is not None and b is not None:
        nums[a], nums[b] = nums[b], nums[a]
        nums[:] = nums[:a+1] + list(reversed(nums[a+1:]))  # reverse suffix to be as less increasing as possible
    else:
        nums.reverse()

