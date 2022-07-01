###########################################################################################
# leetcode problem  https://leetcode.com/problems/kth-largest-element-in-an-array/
###########################################################################################

# RSelect algo implementation
from typing import Optional, List


def pivot_partition(arr: list, l: Optional[int] = None, r: Optional[int] = None) -> int:
    """
    inplace partitioning of the array given

    Returns:
        pivot (int): index of a pivot element in a partitioned array
    """
    if l is None:
        l = 0

    if r is None:
        r = len(arr) - 1

    if l >= r:
        return r

    wall = l - 1
    pivot = arr[r]
    for i in range(l, r):
        current = arr[i]
        if current > pivot:
            continue
        arr[i], arr[wall + 1] = arr[wall + 1], arr[i]
        wall += 1

    arr[r], arr[wall + 1] = arr[wall + 1], arr[r]

    return wall + 1


def findKthLargest(nums: List[int], k: int) -> int:
    l = 0
    r = len(nums) - 1
    rp = len(nums) - k
    while True:
        p = pivot_partition(nums, l, r)
        if p == rp:
            return nums[p]
        if p > rp:
            r = p - 1
        if p < rp:
            l = p + 1


