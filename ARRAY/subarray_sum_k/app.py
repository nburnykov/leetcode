###########################################################################################
# leetcode problem  https://leetcode.com/problems/subarray-sum-equals-k/
###########################################################################################
from typing import List


def subarraySum_my(nums: List[int], k: int) -> int:
    """
    Incorrect implementation based on sliding window, works only with positive numbers
    """

    result = 0
    sums = [0]
    s = 0
    for n in nums:
        s += n
        sums.append(s)

    l, p = 0, 1
    while p != len(sums):
        if l == p:
            s = sums[l]
        else:
            s = sums[p] - sums[l]

        if s == k:
            result += 1
            p += 1
        elif s > k:
            if l == p:
                p += 1
            else:
                l += 1
        else:
            p += 1

    return result


def subarraySum(nums: List[int], k: int) -> int:
    cache = {0: 1}
    s = 0
    result = 0
    for n in nums:
        s += n
        result += cache.get(s - k, 0)  # FIRST we search for sums
        cache[s] = cache.get(s, 0) + 1  # SECOND we update the cache
    return result
