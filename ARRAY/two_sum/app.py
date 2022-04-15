from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    value_hash = dict()
    for i, n in enumerate(nums):
        complement = target - n
        complement_index = value_hash.get(complement)
        if complement_index is None:
            value_hash[n] = i
        else:
            return [i, complement_index]

