from MATRIX.k_smallest_element.app import kthSmallest, le


def test_le_1():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    i = 10
    r = 4
    assert le(matrix, i) == r


def test_le_2():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    i = 13
    r = 8
    assert le(matrix, i) == r


def test_le_3():
    matrix = [[2, 3, 6, 6, 10], [5, 9, 12, 17, 19], [10, 14, 17, 20, 20], [15, 17, 20, 24, 24], [20, 20, 25, 26, 29]]
    i = 6
    r = 5
    assert le(matrix, i) == r



def test_case_1():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    r = 13
    assert kthSmallest(matrix, k) == r


def test_case_2():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 2
    r = 5
    assert kthSmallest(matrix, k) == r


def test_case_3():
    matrix = [[2, 3, 6, 6, 10], [5, 9, 12, 17, 19], [10, 14, 17, 20, 20], [15, 17, 20, 24, 24], [20, 20, 25, 26, 29]]
    k = 4
    r = 6
    assert kthSmallest(matrix, k) == r
