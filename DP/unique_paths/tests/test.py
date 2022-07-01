from DP.unique_paths.app import uniquePaths


def test_case_1():
    m = 3
    n = 7
    r = 28
    assert uniquePaths(m, n) == r


def test_case_2():
    m = 3
    n = 2
    r = 3
    assert uniquePaths(m, n) == r