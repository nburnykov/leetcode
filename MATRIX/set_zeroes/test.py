from MATRIX.set_zeroes.app import setZeroes


def test_case_1():
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_case_2():
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


def test_case_3():
    m = [[1, 0, 3]]
    setZeroes(m)
    assert m == [[0, 0, 0]]
