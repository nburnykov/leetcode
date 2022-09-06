from ARRAY.increasing_triplet_subseq.app import increasingTriplet


def test_case_1():
    nums = [1, 2, 3, 4, 5]
    assert increasingTriplet(nums)


def test_case_2():
    nums = [5, 4, 3, 2, 1]
    assert not increasingTriplet(nums)


def test_case_3():
    nums = [2, 1, 5, 0, 4, 6]
    assert increasingTriplet(nums)


def test_case_4():
    nums = [1, 5, 0, 4, 1, 3]
    assert increasingTriplet(nums)
