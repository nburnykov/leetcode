from ARRAY.group_anagrams.app import groupAnagrams


def test_case_1():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    r = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert groupAnagrams(strs) == r


def test_case_2():
    strs = [""]
    r = [[""]]
    assert groupAnagrams(strs) == r


def test_case_3():
    strs = ["a"]
    r = [["a"]]
    assert groupAnagrams(strs) == r


def test_case_4():
    strs = ["abbbbbbbbbbb","aaaaaaaaaaab"]
    r = [["aaaaaaaaaaab"],["abbbbbbbbbbb"]]
    assert groupAnagrams(strs) == r