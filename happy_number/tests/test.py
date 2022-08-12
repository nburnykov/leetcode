from happy_number.app import isHappy


def test_case_1():
    n = 19
    assert isHappy(n)


def test_case_2():
    n = 2
    assert not isHappy(n)


def test_case_3():
    n = 7
    assert isHappy(n)