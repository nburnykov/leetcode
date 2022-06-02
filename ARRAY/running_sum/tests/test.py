from ARRAY.running_sum.app import runningSum


def test_case_1():
    nums = [1, 2, 3, 4]
    r =[1, 3, 6, 10]
    assert runningSum(nums) == r