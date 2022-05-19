from DFS_BFS.critical_connections.app import criticalConnections
import pickle


def test_case_1():
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    r = [[1, 3]]
    assert criticalConnections(n, connections) == r


def test_case_2():
    n = 2
    connections = [[0, 1]]
    r = [[0, 1]]
    assert criticalConnections(n, connections) == r


def test_case_3():
    n = 5
    connections = [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
    r = [[0, 1]]
    assert criticalConnections(n, connections) == r


def test_case_4():
    n = 10000
    with open('list.pickle', 'rb') as f:
        connections = pickle.load(f)
    r = []
    cc = criticalConnections(n, connections)
    print(len(cc), len(connections))


def test_case_5():
    n = 10
    connections = [
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 3],
        [2, 4],
        [3, 4],
        [3, 5],
        [3, 9],
        [5, 9],
        [5, 6],
        [7, 6],
        [8, 6],
        [8, 7],
    ]
    r = [[5, 6]]
    assert criticalConnections(n, connections) == r


def test_case_6():
    n = 8
    connections = [
        [0, 1],
        [2, 3],
        [2, 4],
        [3, 4],
        [3, 5],
        [3, 6],
        [5, 6],
        [0, 2],
        [1, 2],
        [5, 7]
    ]
    r = [[5, 7]]
    assert criticalConnections(n, connections) == r

