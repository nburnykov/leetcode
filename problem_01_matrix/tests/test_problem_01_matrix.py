from problem_01_matrix.problem_01_matrix import updateMatrix


def test_case_1():
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    output = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert updateMatrix(mat) == output


def test_case_2():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    output = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert updateMatrix(mat) == output
