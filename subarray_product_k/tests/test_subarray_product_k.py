from subarray_product_k.subarray_product_k import numSubarrayProductLessThanK


def test_case_1():
    nums = [10, 5, 2, 6]
    k = 100
    result = 8
    assert numSubarrayProductLessThanK(nums, k) == result


def test_case_2():
    nums = [1, 5, 10, 2, 11, 15, 3, 4, 8, 6, 7, 9]
    k = 100
    result = 25
    assert numSubarrayProductLessThanK(nums, k) == result


def test_case_3():
    nums = [1, 2, 3]
    k = 0
    result = 0
    assert numSubarrayProductLessThanK(nums, k) == result

def test_case_4():
    nums = [1, 1, 1]
    k = 2
    result = 6
    assert numSubarrayProductLessThanK(nums, k) == result