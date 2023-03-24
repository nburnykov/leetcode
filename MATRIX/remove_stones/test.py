from MATRIX.remove_stones.app import removeStones


def test_case_1():
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    result = 5
    assert removeStones(stones) == result


def test_case_2():
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    result = 3
    assert removeStones(stones) == result


def test_case_3():
    stones = [[0, 0]]
    result = 0
    assert removeStones(stones) == result


def test_case_4():
    stones = [[4, 4], [5, 5], [3, 1], [1, 4], [1, 1], [2, 3], [0, 3], [2, 4], [3, 5]]
    result = 8
    assert removeStones(stones) == result
