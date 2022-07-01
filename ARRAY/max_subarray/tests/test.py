from ARRAY.max_subarray.app import maxSubArray


def test_case_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    r = 6
    assert maxSubArray(nums) == r

def test_case_2():
    nums = [1]
    r = 1
    assert maxSubArray(nums) == r

def test_case_3():
    nums = [5,4,-1,7,8]
    r = 23
    assert maxSubArray(nums) == r

def test_case_4():
    nums = [-2, -1]
    r = -1
    assert maxSubArray(nums) == r