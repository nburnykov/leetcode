from MATRIX.range_sum.app import NumMatrix


def test_case_1():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    boundary_1 = [2, 1, 4, 3]
    boundary_2 = [1, 1, 2, 2]
    boundary_3 = [1, 2, 2, 4]
    sm = NumMatrix(matrix)
    assert sm.sumRegion(*boundary_1) == 8
    assert sm.sumRegion(*boundary_2) == 11
    assert sm.sumRegion(*boundary_3) == 12