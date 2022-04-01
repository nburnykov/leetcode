from two_sorted_arrays_median.two_sorted_arrays_median import findMedianSortedArrays


def test_case_1():
    nums1 = [1, 3]
    nums2 = [2]
    output = 2.0
    assert findMedianSortedArrays(nums1, nums2) == output


def test_case_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    output = 2.5
    assert findMedianSortedArrays(nums1, nums2) == output


def test_case_3():
    nums1 = []
    nums2 = [3, 4]
    output = 3.5
    assert findMedianSortedArrays(nums1, nums2) == output
