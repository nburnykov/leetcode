from minimum_size_sum.minimum_size_sum import minSubArrayLen


def test_case_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = 2
    assert minSubArrayLen(target, nums) == result


def test_case_2():
    target = 4
    nums = [1, 4, 4]
    result = 1
    assert minSubArrayLen(target, nums) == result


def test_case_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    result = 0
    assert minSubArrayLen(target, nums) == result
