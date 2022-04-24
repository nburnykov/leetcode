from ARRAY.permutations_2.app import permuteUnique


def test_case_1():
    n = [1, 1, 2]
    r = [[1, 1, 2],
         [1, 2, 1],
         [2, 1, 1]]

    assert permuteUnique(n) == r


def test_case_2():
    n = [1, 2, 3]
    r = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    assert permuteUnique(n) == r
