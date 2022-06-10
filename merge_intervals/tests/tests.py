from merge_intervals.app import merge


def test_case_1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    r = [[1, 6], [8, 10], [15, 18]]
    assert merge(intervals) == r


def test_case_2():
    intervals = [[1, 4], [4, 5]]
    r = [[1, 5]]
    assert merge(intervals) == r
