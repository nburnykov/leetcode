from DP.combination_sum_4.app import combinationSum4


def test_case_1():
    nums = [1, 2, 3]
    target = 4
    r = 7
    assert combinationSum4(nums, target) == r


def test_case_2():
    nums = [9]
    target = 3
    r = 0
    assert combinationSum4(nums, target) == r


def test_case_3():
    nums = [4,2,1]
    target = 32
    r = 0
    assert combinationSum4(nums, target) == r