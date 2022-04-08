###########################################################################################
# leetcode problem https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
###########################################################################################
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    # corner cases
    if len(nums) == 0:
        return [-1, -1]
    if nums[0] == nums[-1] and nums[0] != target:
        return [-1, -1]

    leftmost = 0 if nums[0] == target else None
    rightmost = len(nums) - 1 if nums[-1] == target else None

    # find leftmost index
    if leftmost is None:
        l, r = 1, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
                continue
            if nums[mid] > target:
                r = mid - 1
                continue

            if nums[mid] == target and nums[mid - 1] < nums[mid]:
                leftmost = mid
                break
            else:
                r = mid - 1

    if leftmost is None:
        return [-1, -1]

    # find rightmost index
    if rightmost is None:
        l, r = leftmost, len(nums) - 2
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
                continue
            if nums[mid] > target:
                r = mid - 1
                continue

            if nums[mid] == target and nums[mid + 1] > nums[mid]:
                rightmost = mid
                break
            else:
                l = mid + 1

    return [leftmost, rightmost]
