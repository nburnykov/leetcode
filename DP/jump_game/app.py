from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:  # corner case
        return True

    jump_index = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= jump_index:
            jump_index = i
    return jump_index == 0
