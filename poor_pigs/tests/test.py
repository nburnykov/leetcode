from poor_pigs.app import poorPigs


def test_case_1():
    buckets = 4
    minutesToDie = 15
    minutesToTest = 15
    r = 2
    assert poorPigs(buckets, minutesToDie, minutesToTest) == r


def test_case_2():
    buckets = 1
    minutesToDie = 15
    minutesToTest = 15
    r = 0
    assert poorPigs(buckets, minutesToDie, minutesToTest) == r


def test_case_3():
    buckets = 2
    minutesToDie = 15
    minutesToTest = 15
    r = 1
    assert poorPigs(buckets, minutesToDie, minutesToTest) == r


def test_case_4():
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    r = 5
    assert poorPigs(buckets, minutesToDie, minutesToTest) == r
