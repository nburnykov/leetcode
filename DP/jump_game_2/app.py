from typing import List


def jump(nums: List[int]) -> int:
    jump_count, jump_max, jump_current = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] > jump_max:
            jump_max = nums[i]

        if jump_current == 0:  # end of the current jump
            jump_current = jump_max  # switch to the maximum length jump that was covered by the current
            if i < len(nums) - 1:  # if the end wasn't reached register the next jump
                jump_count += 1

        jump_max -= 1
        jump_current -= 1

    return jump_count
