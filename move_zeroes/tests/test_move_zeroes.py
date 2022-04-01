from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_indexes = []
    for i, n in enumerate(nums):
        if n == 0:
            zero_indexes.append(i)

    for i in zero_indexes[::-1]:
        nums.pop(i)

    nums.extend([0]*len(zero_indexes))

    return

