from rotting_oranges.rotting_oranges import orangesRotting


def test_case_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    output = 4
    assert orangesRotting(grid) == output


def test_case_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    output = -1
    assert orangesRotting(grid) == output


def test_case_3():
    grid = [[0,2]]
    output = 0
    assert orangesRotting(grid) == output
