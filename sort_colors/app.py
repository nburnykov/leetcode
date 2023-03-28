###########################################################################################
# leetcode problem  https://leetcode.com/problems/sort-colors/
###########################################################################################
from typing import List


def sortColors(nums: List[int]):
    """
    QuickSort implementation
    """

    def srt(nums: List[int], ps: int, pe: int):
        p_left, p_right = ps, pe
        if p_right - p_left <= 0:
            return
        if p_right - p_left == 1:
            if nums[p_left] > nums[p_left + 1]:
                nums[p_left], nums[p_left + 1] = nums[p_left + 1], nums[p_left]
            return

        pivot = nums[p_right]  # select pivot as the last element

        while p_right - p_left > 0:
            if nums[p_left] <= pivot:  # if less than pivot then left it on its position
                p_left += 1
                continue
            if nums[p_left] > pivot >= nums[p_right]:  # if on both sides from pivot then swap
                nums[p_left], nums[p_right] = nums[p_right], nums[p_left]
                continue
            p_right -= 1  # if p_left > pivot and p_right > pivot

        srt(nums, ps, p_left - 1)
        srt(nums, p_left, pe)

    srt(nums, 0, len(nums) - 1)
