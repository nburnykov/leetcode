###########################################################################################
# leetcode problem https://leetcode.com/problems/permutations/
###########################################################################################

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    if len(nums) == 2:
        return [nums, nums[::-1]]
    else:
        num_set = set(nums)
        result = []
        for n in num_set:
            permutations = permute(list(num_set - {n}))
            ir = [[n, *p] for p in permutations]
            result.extend(ir)
        return result
