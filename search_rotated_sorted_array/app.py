###########################################################################################
# leetcode problem https://leetcode.com/problems/search-in-rotated-sorted-array/
###########################################################################################

from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l

        if (target > nums[l]) and (nums[mid] >= nums[l]):
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            continue

        if (target < nums[r]) and (nums[mid] <= nums[r]):
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            continue

        if nums[mid] < target:
            r = mid - 1
        else:
            l = mid + 1

    return -1
