from DFS_BFS.perfect_squares.app import numSquares


def test_case_1():
    n = 12
    r = 3
    assert numSquares(n) == r


def test_case_2():
    n = 13
    r = 2
    assert numSquares(n) == r
