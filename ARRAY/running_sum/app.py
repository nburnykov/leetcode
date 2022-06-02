###########################################################################################
# leetcode problem https://leetcode.com/problems/running-sum-of-1d-array/
###########################################################################################

from typing import List


def runningSum(nums: List[int]) -> List[int]:
    sum = 0
    result = []
    for n in nums:
        sum += n
        result.append(sum)

    return result