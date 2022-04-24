from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    if len(nums) < 2:
        return [nums]
    if len(nums) == 2:
        if nums[0] != nums[1]:
            return [nums, nums[::-1]]
        else:
            return [nums]

    nums.sort()
    result = []
    for i in range(0, len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        permutations = permuteUnique(nums[:i] + nums[i + 1:])
        for p in permutations:
            result.append([nums[i], *p])

    return result
