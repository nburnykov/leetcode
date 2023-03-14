from ARRAY.longest_repeating_character_replacement.app import characterReplacement


def test_case_1():
    s = "ABAB"
    k = 2
    r = 4
    assert characterReplacement(s, k) == r


def test_case_2():
    s = "AABABBA"
    k = 1
    r = 4
    assert characterReplacement(s, k) == r


def test_case_3():
    s = "AAAAA"
    k = 0
    r = 5
    assert characterReplacement(s, k) == r