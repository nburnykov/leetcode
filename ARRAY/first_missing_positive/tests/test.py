from ARRAY.first_missing_positive.app import firstMissingPositive


def test_case_1():
    nums = [1, 2, 0]
    r = 3
    assert firstMissingPositive(nums) == r


def test_case_2():
    nums = [1, 0, 2]
    r = 3
    assert firstMissingPositive(nums) == r


def test_case_3():
    nums = [1, 2, 3]
    r = 4
    assert firstMissingPositive(nums) == r


def test_case_4():
    nums = [3, 4, -1, 1]
    r = 2
    assert firstMissingPositive(nums) == r


def test_case_5():
    nums = [2]
    r = 1
    assert firstMissingPositive(nums) == r


def test_case_6():
    nums = [1, 1]
    r = 2
    assert firstMissingPositive(nums) == r


def test_case_7():
    nums = [2, 2]
    r = 1
    assert firstMissingPositive(nums) == r