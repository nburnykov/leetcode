from DFS_BFS.shortest_path_matrix.app import shortestPathBinaryMatrix


def test_case_1():
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    result = 4
    assert shortestPathBinaryMatrix(grid) == result

def test_case_2():
    grid = [[0,1],[1,0]]
    result = 2
    assert shortestPathBinaryMatrix(grid) == result

def test_case_3():
    grid = [[0,0,0],[1,0,0],[1,1,0]]
    result = 3
    assert shortestPathBinaryMatrix(grid) == result

def test_case_4():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    result = 4
    assert shortestPathBinaryMatrix(grid) == result