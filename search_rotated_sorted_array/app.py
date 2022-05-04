###########################################################################################
# leetcode problem https://leetcode.com/problems/search-in-rotated-sorted-array/
###########################################################################################

from typing import List


def search2(nums: List[int], target: int) -> int:
    # corner cases
    if len(nums) == 0:
        return -1
    if len(nums) < 3:
        result = 0 if target == nums[0] else -1
        if result == -1:
            result = len(nums) - 1 if target == nums[-1] else -1
        return result

    last_index = len(nums) - 1
    if nums[0] < nums[last_index]:  # array has not been rotated
        l, r = 0, last_index
    else:
        l, r = 1, last_index
        while True:  # search for a pivot
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                pivot = mid
                break
            if nums[mid] >= nums[0]:
                l = mid + 1
            if nums[mid] <= nums[last_index]:
                r = mid - 1

        if target >= nums[0]:  # search in a left part of array
            l, r = 0, pivot
        else:  # in a right
            l, r = pivot, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


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