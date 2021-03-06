from typing import List


def findMin(nums: List[int]) -> int:
    # corner cases
    if len(nums) == 0:
        return 0
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[l]:
            l = mid
        if nums[mid] < nums[r]:
            r = mid
        if r - l == 1:
            return nums[r]

