###########################################################################################
# leetcode problem https://leetcode.com/problems/majority-element/
###########################################################################################
from typing import List


def majorityElement(nums: List[int]) -> int:
    """
    Boyer–Moore majority vote algorithm

    Can be applied only to cases where the majority element appears more than n/2 times in the array

    :param nums:
    :return:
    """
    major = None
    major_count = 0
    for n in nums:
        if major_count > 0:
            if n == major:
                major_count += 1
            else:
                major_count -= 1
        if major_count == 0:
            major = n
            major_count += 1
    return major