from ARRAY.max_area_cuts.app import maxArea


def test_case_1():
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    r = 4
    assert maxArea(h, w, horizontalCuts, verticalCuts) == r

def test_case_2():
    h = 5
    w = 4
    horizontalCuts = [3, 1]
    verticalCuts = [1]
    r = 6
    assert maxArea(h, w, horizontalCuts, verticalCuts) == r

def test_case_3():
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    r = 9
    assert maxArea(h, w, horizontalCuts, verticalCuts) == r