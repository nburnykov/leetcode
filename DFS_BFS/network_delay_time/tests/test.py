from DFS_BFS.network_delay_time.app import networkDelayTime, networkDelayTimeHeap


def test_case_1():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    r = 2
    assert networkDelayTime(times, n, k) == r


def test_case_2():
    times = [[1, 2, 1]]
    n = 2
    k = 1
    r = 1
    assert networkDelayTime(times, n, k) == r


def test_case_3():
    times = [[1, 2, 1]]
    n = 2
    k = 2
    r = -1
    assert networkDelayTime(times, n, k) == r


def test_case_special_1():
    times = [[1, 2, 100], [1, 3, 1], [2, 4, 1], [3, 4, 250]]
    k = 1
    n = 4
    r = 101
    assert networkDelayTimeHeap(times, n, k) == r

def test_case_special_2():
    times = [[1, 2, 1], [1, 3, 5], [2, 4, 510], [3, 5, 5], [5, 6, 5], [6, 4, 5]]
    k = 1
    n = 6
    r = 20
    assert networkDelayTimeHeap(times, n, k) == r