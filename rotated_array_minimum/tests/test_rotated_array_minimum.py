from rotated_array_minimum.rotated_array_minimum import findMin


def test_case_1():
    nums = [3, 4, 5, 1, 2]
    min = 1
    assert findMin(nums) == min


def test_case_2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    min = 0
    assert findMin(nums) == min

def test_case_3():
    nums = [2, 1]
    min = 1
    assert findMin(nums) == min

def test_case_4():
    nums = [3, 1, 2]
    min = 1
    assert findMin(nums) == min
