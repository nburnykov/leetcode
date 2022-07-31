from bitwise_range.app import rangeBitwiseAnd


def test_case_1():
    left = 5
    right = 7
    r = 4
    assert rangeBitwiseAnd(left, right) == r

def test_case_2():
    left = 1
    right = 2147483647
    r = 0
    assert rangeBitwiseAnd(left, right) == r

def test_case_3():
    left = 2
    right = 4
    r = 0
    assert rangeBitwiseAnd(left, right) == r

def test_case_4():
    left = 5
    right = 5
    r = 5
    assert rangeBitwiseAnd(left, right) == r

def test_case_5():
    left = 2
    right = 6
    r = 0
    assert rangeBitwiseAnd(left, right) == r