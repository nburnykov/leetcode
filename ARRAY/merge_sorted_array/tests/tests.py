from ARRAY.merge_sorted_array.app import merge


def test_case_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    r = [1, 2, 2, 3, 5, 6]
    merge(nums1, m, nums2, n)
    assert nums1 == r


def test_case_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    r = [1]
    merge(nums1, m, nums2, n)
    assert nums1 == r


def test_case_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    r = [1]
    merge(nums1, m, nums2, n)
    assert nums1 == r


def test_case_4():
    nums1 = [1, 0]
    m = 1
    nums2 = [2]
    n = 1
    r = [1, 2]
    merge(nums1, m, nums2, n)
    assert nums1 == r