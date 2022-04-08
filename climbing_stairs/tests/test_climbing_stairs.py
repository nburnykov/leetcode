from climbing_stairs.climbing_stairs import climbStairs


def test_case_1():
    n = 2
    r = 2
    assert climbStairs(n) == r


def test_case_2():
    n = 3
    r = 3
    assert climbStairs(n) == r


def test_case_3():
    n = 29
    r = 832040
    assert climbStairs(n) == r


def test_case_4():
    n = 35
    r = 14930352
    assert climbStairs(n) == r


def test_case_5():
    n = 5
    r = 8
    assert climbStairs(n) == r