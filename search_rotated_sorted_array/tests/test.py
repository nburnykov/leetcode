from search_rotated_sorted_array.app import search


def test_case_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    out = 4
    assert search(nums, target) == out


def test_case_2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    out = -1
    assert search(nums, target) == out


def test_case_3():
    nums = [1]
    target = 0
    out = -1
    assert search(nums, target) == out


def test_case_4():
    nums = [1, 3, 5]
    target = 0
    out = -1
    assert search(nums, target) == out


def test_case_5():
    nums = [1, 3, 5]
    target = 1
    out = 0
    assert search(nums, target) == out


def test_case_6():
    nums = [1, 3, 5]
    target = 3
    out = 1
    assert search(nums, target) == out


def test_case_7():
    nums = [1, 3, 5]
    target = 5
    out = 2
    assert search(nums, target) == out


def test_case_8():
    nums = [3, 5, 1]
    target = 1
    out = 2
    assert search(nums, target) == out