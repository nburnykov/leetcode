from pascals_triangle.app import getRow


def test_case_1():
    rowIndex = 3
    r = [1, 3, 3, 1]
    assert getRow(rowIndex) == r


def test_case_2():
    rowIndex = 0
    r = [1]
    assert getRow(rowIndex) == r


def test_case_3():
    rowIndex = 1
    r = [1, 1]
    assert getRow(rowIndex) == r