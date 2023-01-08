from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums.append(9999)
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
    nums.pop(-1)
    return len(nums)