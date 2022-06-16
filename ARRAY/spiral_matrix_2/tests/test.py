from ARRAY.spiral_matrix_2.app import generateMatrix


def test_case_1():
    n = 3
    r = [[1,2,3],[8,9,4],[7,6,5]]
    assert generateMatrix(n) == r

def test_case_2():
    n = 1
    r = [[1]]
    assert generateMatrix(n) == r