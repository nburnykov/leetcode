###########################################################################################
# leetcode problem  https://leetcode.com/problems/maximum-subarray/
###########################################################################################
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Kadane's algo
    Current max is either prev_max + current_element or current element if this is bigger than prev_max

    """
    sums = [float("-inf")]
    for n in nums:
        sums.append(max(n, n + sums[-1]))
    return max(sums)

