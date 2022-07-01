from DP.decode_ways.app import numDecodings


def test_case_1():
    s = "12"
    r = 2
    assert numDecodings(s) == r


def test_case_2():
    s = "226"
    r = 3
    assert numDecodings(s) == r


def test_case_3():
    s = "06"
    r = 0
    assert numDecodings(s) == r


def test_case_4():
    s = "27"
    r = 1
    assert numDecodings(s) == r
