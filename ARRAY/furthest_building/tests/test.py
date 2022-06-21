from ARRAY.furthest_building.app import furthestBuilding


def test_case_1():
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    r = 4
    assert furthestBuilding(heights, bricks, ladders) == r


def test_case_2():
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    r = 7
    assert furthestBuilding(heights, bricks, ladders) == r


def test_case_3():
    heights = [14, 3, 19, 3]
    bricks = 17
    ladders = 0
    r = 3
    assert furthestBuilding(heights, bricks, ladders) == r

def test_case_4():
    heights = [14]
    bricks = 17
    ladders = 17
    r = 0
    assert furthestBuilding(heights, bricks, ladders) == r
