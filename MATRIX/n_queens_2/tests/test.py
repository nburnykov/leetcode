from MATRIX.n_queens_2.app import totalNQueens


def test_case_1():
    n = 4
    r = 2
    assert totalNQueens(n) == r

def test_case_2():
    n = 1
    r = 1
    assert totalNQueens(n) == r