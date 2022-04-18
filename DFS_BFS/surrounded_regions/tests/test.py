from DFS_BFS.surrounded_regions.app import solve


def test_case_1():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    result = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    solve(board)
    assert board == result


def test_case_2():
    board = [["X"]]
    result = [["X"]]
    solve(board)
    assert board == result


def test_case_3():
    board = [["O"]]
    result = [["O"]]
    solve(board)
    assert board == result


def test_case_4():
    board = [["O","O"],["O","O"]]
    result = [["O","O"],["O","O"]]
    solve(board)
    assert board == result