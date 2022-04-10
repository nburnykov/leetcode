from typing import List


def findPeakElement(nums: List[int]) -> int:
    # corner cases
    if len(nums) == 1:
        return 0

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        val_left = nums[mid - 1] if mid > 0 else float("-inf")
        val_right = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")
        if nums[mid] >= max(val_right, val_left):
            return mid
        if nums[mid] < val_left:
            r = mid - 1
            continue  # in case if mid element is a minimal one go left
        if nums[mid] < val_right:
            l = mid + 1




