from typing import List


def singleNumber(nums: List[int]) -> int:
    num = 0
    for n in nums:
        num = num ^ n

    return num