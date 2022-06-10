from ARRAY.insert_interval.app import insert


def test_case_1():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    r = [[1, 5], [6, 9]]
    assert insert(intervals, newInterval) == r


def test_case_2():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    r = [[1, 2], [3, 10], [12, 16]]
    assert insert(intervals, newInterval) == r


def test_case_3():
    intervals = []
    newInterval = [4, 8]
    r = [[4, 8]]
    assert insert(intervals, newInterval) == r

def test_case_4():
    intervals = [[2,5],[6,7],[8,9]]
    newInterval = [0, 1]
    r = [[0,1],[2,5],[6,7],[8,9]]
    assert insert(intervals, newInterval) == r

