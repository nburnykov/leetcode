from integer_break.app import integerBreak


def test_case_1():
    n = 2
    r = 1
    assert integerBreak(n) == r


def test_case_2():
    n = 10
    r = 36
    assert integerBreak(n) == r

def test_case_3():
    n = 5
    r = 6
    assert integerBreak(n) == r