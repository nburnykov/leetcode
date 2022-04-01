###########################################################################################
# leetcode problem https://leetcode.com/problems/binary-search/
###########################################################################################
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        pivot_prev = None
        while True:
            pivot = (l + r) // 2

            if nums[pivot] == target:  # case 1
                return pivot

            if nums[pivot] > target:  # case 2
                r = pivot - 1

            else:  # case 3
                l = pivot + 1

            if pivot == pivot_prev:
                return -1

            pivot_prev = pivot
