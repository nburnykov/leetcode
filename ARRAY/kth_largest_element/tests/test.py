from ARRAY.kth_largest_element.app import pivot_partition, findKthLargest


def test_partition_1():
    a = [4, 6, 8, 1, 4, 2, 1]
    p = pivot_partition(a)
    assert a == [1, 1, 8, 4, 4, 2, 6]
    assert p == 1


def test_partition_2():
    a = [4]
    p = pivot_partition(a)
    assert a == [4]
    assert p == 0


def test_partition_3():
    a = [4, 1]
    p = pivot_partition(a)
    assert a == [1, 4]
    assert p == 0


def test_partition_4():
    a = [0, 0, 0, 0, 0, 0]
    p = pivot_partition(a)
    assert a == [0, 0, 0, 0, 0, 0]
    assert p == 5


def test_case_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    r = 5
    assert findKthLargest(nums, k) == r


def test_case_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    r = 4
    assert findKthLargest(nums, k) == r
