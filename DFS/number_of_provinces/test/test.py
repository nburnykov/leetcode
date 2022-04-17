from DFS.number_of_provinces.app import findCircleNum


def test_case_1():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = 2
    assert findCircleNum(isConnected) == result


def test_case_2():
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result = 3
    assert findCircleNum(isConnected) == result


def test_case_3():
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    result = 1
    assert findCircleNum(isConnected) == result
