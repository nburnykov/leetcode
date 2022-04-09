from search_2d_matrix.search_2d_matrix import searchMatrix


def test_case_1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert searchMatrix(matrix, target)

def test_case_2():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert not searchMatrix(matrix, target)

def test_case_3():
    matrix = [[1],[3]]
    target = 3
    assert searchMatrix(matrix, target)