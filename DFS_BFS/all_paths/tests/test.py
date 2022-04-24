from DFS_BFS.all_paths.app import allPathsSourceTarget


def test_case_1():
    g = [[1, 2], [3], [3], []]
    r = [[0, 1, 3], [0, 2, 3]]
    assert allPathsSourceTarget(g) == r


def test_case_2():
    g = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    r = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert allPathsSourceTarget(g) == r
