###########################################################################################
# leetcode problem  https://leetcode.com/problems/sort-colors/
###########################################################################################
from typing import List


def sortColors(nums: List[int]):
    """
    QuickSort implementation
    """

    def srt(nums: List[int], ps: int, pe: int):
        p1, p2 = ps, pe
        if p2 - p1 <= 0:
            return
        if p2 - p1 == 1:
            if nums[p1] > nums[p1 + 1]:
                nums[p1], nums[p1 + 1] = nums[p1 + 1], nums[p1]
            return

        pivot = nums[p2]  # select pivot as the last element

        while p2 - p1 > 0:
            if nums[p1] <= pivot:  # if less than pivot then left it on its position
                p1 += 1
                continue
            if nums[p1] > pivot >= nums[p2]:  # if on both sides from pivot then swap
                nums[p1], nums[p2] = nums[p2], nums[p1]
                continue
            p2 -= 1  # if p1 > pivot and p2 > pivot

        srt(nums, ps, p1 - 1)
        srt(nums, p1, pe)

    srt(nums, 0, len(nums) - 1)
