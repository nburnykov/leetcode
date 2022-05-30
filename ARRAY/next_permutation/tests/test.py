from ARRAY.next_permutation.app import nextPermutation


def test_case_1():
    nums = [1, 2, 3]
    r = [1, 3, 2]
    nextPermutation(nums)
    assert nums == r


def test_case_2():
    nums = [1, 1, 5]
    r = [1, 5, 1]
    nextPermutation(nums)
    assert nums == r


def test_case_3():
    nums = [3, 2, 1]
    r = [1, 2, 3]
    nextPermutation(nums)
    assert nums == r


def test_case_4():
    nums = [1, 2]
    r = [2, 1]
    nextPermutation(nums)
    assert nums == r


def test_case_5():
    nums = [1, 3, 2]
    r = [2, 1, 3]
    nextPermutation(nums)
    assert nums == r

