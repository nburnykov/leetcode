from BINARY_SEARCH.binary_search_.app import Solution, search


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = search(nums, target)
    assert result == 4


def test_case_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = search(nums, target)
    assert result == -1


def test_case_3():
    nums = [2, 5]
    target = 2
    result = search(nums, target)
    assert result == 0


def test_case_4():
    nums = [-1, 0, 3, 5, 9, 12]
    target = -1
    result = search(nums, target)
    assert result == 0


def test_case_5():
    nums = [2, 5]
    target = 5
    result = search(nums, target)
    assert result == 1


def test_case_6():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 13
    result = search(nums, target)
    assert result == 4
