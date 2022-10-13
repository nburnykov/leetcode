from ARRAY.where_will_ball_fall.app import findBall


def test_case_1():
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    result = [1, -1, -1, -1, -1]
    assert findBall(grid) == result


def test_case_2():
    grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
    result = [0, 1, 2, 3, 4, -1]
    assert findBall(grid) == result

def test_case_3():
    grid = [[-1]]
    result = [-1]
    assert findBall(grid) == result