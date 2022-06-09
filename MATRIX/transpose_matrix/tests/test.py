from MATRIX.transpose_matrix.app import transpose


def test_case_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose(matrix) == r

def test_case_2():
    matrix = [[1, 2, 3], [4, 5, 6]]
    r = [[1,4],[2,5],[3,6]]
    assert transpose(matrix) == r
