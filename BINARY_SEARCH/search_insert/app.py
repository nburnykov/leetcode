from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pointer = len(nums)
        pointer = pointer // 2
        pointer_prev = 0
        while True:
            value = nums[pointer]

            if pointer == 0 and value >= target:
                return 0

            if pointer == len(nums) - 1 and value < target:
                return len(nums)

            value_prev = nums[pointer - 1]

            if value_prev < target <= value:
                return pointer

            step = abs(pointer - pointer_prev) // 2
            if step == 0:
                step = 1
            pointer_prev = pointer

            if value > target and value_prev >= target:
                pointer = pointer - step

            if value < target:
                pointer = pointer + step