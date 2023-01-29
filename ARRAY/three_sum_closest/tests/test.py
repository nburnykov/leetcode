from ARRAY.three_sum_closest.app import threeSumClosest


def test_case_1():
    n = [-1, 2, 1, -4]
    t = 1
    r = 2
    assert threeSumClosest(n, t) == r


def test_case_2():
    n = [0, 0, 0]
    t = 1
    r = 0
    assert threeSumClosest(n, t) == r


def test_case_3():
    n = [1, 1, 1, 0]
    t = -100
    r = 2
    assert threeSumClosest(n, t) == r


def test_case_4():
    n = [0,3,97,102,200]
    t = 300
    r = 300
    assert threeSumClosest(n, t) == r
