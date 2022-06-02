from MATRIX.spiral_order.app import spiralOrder


def test_case_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiralOrder(matrix) == r


def test_case_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    r = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiralOrder(matrix) == r
