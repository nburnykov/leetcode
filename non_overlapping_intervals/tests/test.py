from non_overlapping_intervals.app import eraseOverlapIntervals


def test_case_1():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    r = 1
    assert eraseOverlapIntervals(intervals) == r


def test_case_2():
    intervals = [[1, 2], [1, 2], [1, 2]]
    r = 2
    assert eraseOverlapIntervals(intervals) == r


def test_case_3():
    intervals = [[1, 2], [2, 3]]
    r = 0
    assert eraseOverlapIntervals(intervals) == r