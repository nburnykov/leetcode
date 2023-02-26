# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        p = (l + r) // 2
        a, b, c = nums[l], nums[p], nums[r]
        if a == target or b == target or c == target:
            return True

        if a == b == c:  # we don't know where to search so check every element between r and l
            for n in nums[l:r + 1]:
                if n == target:
                    return True
            return False

        if (target > a and b >= a) or (target < c and b <= c):  # same slope
            if target < b:
                r = p - 1
            else:
                l = p + 1

            continue

        if target < b:  # different slopes
            l = p + 1
        else:
            r = p - 1

    return False
