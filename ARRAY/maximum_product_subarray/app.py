# https://leetcode.com/problems/maximum-product-subarray
from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    Modified Kadane's algo: find MAX and MIN value on each step
    """
    result = float("-inf")
    arr_min, arr_max = 1, 1
    for n in nums:
        prod1 = arr_min * n
        prod2 = arr_max * n
        arr_max = max(n, max(prod1, prod2))
        arr_min = min(n, min(prod1, prod2))
        result = max(result, arr_max)

    return result


