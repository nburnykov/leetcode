from ARRAY.search_range.app import searchRange


def test_case_1():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    output = [3, 4]
    assert searchRange(nums, target) == output


def test_case_2():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    output = [-1, -1]
    assert searchRange(nums, target) == output

def test_case_3():
    nums = [1, 3]
    target = 1
    output = [0, 0]
    assert searchRange(nums, target) == output

def test_case_4():
    nums = [1, 4]
    target = 4
    output = [1, 1]
    assert searchRange(nums, target) == output

def test_case_5():
    nums = [1,2,3]
    target = 3
    output = [2, 2]
    assert searchRange(nums, target) == output
