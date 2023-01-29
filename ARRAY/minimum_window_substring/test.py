from ARRAY.minimum_window_substring.app import minWindow


def test_case_1():
    s = "ADOBECODEBANC"
    t = "ABC"
    r = "BANC"
    assert minWindow(s, t) == r


def test_case_2():
    s = "A"
    t = "A"
    r = "A"
    assert minWindow(s, t) == r


def test_case_3():
    s = "A"
    t = "AA"
    r = ""
    assert minWindow(s, t) == r