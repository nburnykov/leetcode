from graycode.app import grayCode


def test_case_1():
    n = 2
    r = [0,1, 3, 2]
    assert grayCode(n) == r

def test_case_2():
    n = 1
    r = [0,1]
    assert grayCode(n) == r