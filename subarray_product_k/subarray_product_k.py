###########################################################################################
# leetcode problem https://leetcode.com/problems/subarray-product-less-than-k/
###########################################################################################
from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    p2, product = 0, 1
    result = 0
    for p1 in range(len(nums)):
        product *= nums[p1]
        while product >= k and p2 <= p1:
            product /= nums[p2]
            p2 += 1
        result += p1 - p2 + 1
    return result
