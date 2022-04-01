###########################################################################################
# leetcode problem https://leetcode.com/problems/median-of-two-sorted-arrays/
###########################################################################################
from typing import List


def median(a: list) -> float:
    median_index = len(a) // 2
    if len(a) % 2 == 0:
        return (a[median_index] + a[median_index - 1]) / 2
    else:
        return a[median_index]


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    arr_a, arr_b = nums1, nums2

    # initial corner cases
    if len(arr_a) == 0:
        return median(arr_b)
    if len(arr_b) == 0:
        return median(arr_a)

    if len(arr_b) < len(arr_a):
        arr_a, arr_b = arr_b, arr_a

    length_composed = len(arr_a) + len(arr_b) + 1

    l, r = 0, len(arr_a) - 1

    while True:
        median_index_a = (l + r) // 2
        median_index_b = length_composed // 2 - median_index_a - 2

        left_a = arr_a[median_index_a] if median_index_a >= 0 else float('-inf')
        left_b = arr_b[median_index_b] if median_index_b >= 0 else float('-inf')
        right_a = arr_a[median_index_a + 1] if median_index_a + 1 < len(arr_a) else float('inf')
        right_b = arr_b[median_index_b + 1] if median_index_b + 1 < len(arr_b) else float('inf')

        if left_a <= right_b and left_b <= right_a:
            if (len(arr_a) + len(arr_b)) % 2 == 0:
                return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
            return max(left_a, left_b)

        if left_a > right_b:  # true binary search
            r = median_index_a - 1
        else:
            l = median_index_a + 1




