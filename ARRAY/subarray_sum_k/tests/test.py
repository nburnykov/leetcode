from ARRAY.subarray_sum_k.app import subarraySum


def test_case_1():
    nums = [1, 1, 1]
    k = 2
    r = 2
    assert subarraySum(nums, k) == r


def test_case_2():
    nums = [1, 2, 3]
    k = 3
    r = 2
    assert subarraySum(nums, k) == r


def test_case_3():
    nums = [1]
    k = 1
    r = 1
    assert subarraySum(nums, k) == r


def test_case_4():
    nums = [1]
    k = 1
    r = 1
    assert subarraySum(nums, k) == r


def test_case_5():
    nums = [-1, -1, 1]
    k = 0
    r = 1
    assert subarraySum(nums, k) == r


def test_case_6():
    nums = [0, 0, 1, 1, 0, 0, 1, 0]
    k = 3
    r = 1
    assert subarraySum(nums, k) == r
