###########################################################################################
# leetcode problem  https://leetcode.com/problems/arithmetic-slices/
###########################################################################################

from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    ln = 0
    diff = None
    result = 0
    for n in range(1, len(nums)):
        d = nums[n - 1] - nums[n]
        if d != diff:   # in case of new diff reset saved diff and sequence length to 1
            ln = 1
            diff = d
            continue

        ln += 1
        slice_count = ln - 2 + 1   # in case of 2 equal diffs (3 elements) - 1 slice, 4 elements - 2 slices etc.
        if slice_count > 0:
            result += slice_count

    return result
