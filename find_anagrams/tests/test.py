from find_anagrams.app import findAnagrams


def test_case_1():
    s = "cbaebabacd"
    p = "abc"
    r = [0, 6]
    assert findAnagrams(s, p) == r

def test_case_2():
    s = "abab"
    p = "ab"
    r = [0, 1, 2]
    assert findAnagrams(s, p) == r

def test_case_3():
    s = "ababababab"
    p = "aab"
    r = [0,2,4,6]
    assert findAnagrams(s, p) == r