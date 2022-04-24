from ARRAY.subsets.app import subsets


def test_case_1():
    nums = [1, 2, 3]
    result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert subsets(nums) == result


def test_case_2():
    nums = [0]
    result = [[], [0]]
    assert subsets(nums) == result
