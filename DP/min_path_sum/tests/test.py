from DP.min_path_sum.app import minPathSum


def test_case_1():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    r = 7
    assert minPathSum(grid) == r


def test_case_2():
    grid = [[1,2,3],[4,5,6]]
    r = 12
    assert minPathSum(grid) == r


def test_case_3():
    grid = [[0,0],[0,0]]
    r = 0
    assert minPathSum(grid) == r