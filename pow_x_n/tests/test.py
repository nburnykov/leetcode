from pow_x_n.app import myPow


def test_case_1():
    x = 2.0
    n = 10
    r = 1024.0
    assert myPow(x, n) == r

def test_case_2():
    x = 2.1
    n = 3
    r = 9.261
    assert myPow(x, n) == r

def test_case_3():
    x = 2
    n = -2
    r = 0.25
    assert myPow(x, n) == r