from ARRAY.word_break.app import wordBreak, find_all_lengths


def test_case_1():
    s = "leetcode"
    wordDict = ["leet", "code"]
    assert wordBreak(s, wordDict)


def test_case_2():
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert wordBreak(s, wordDict)


def test_case_3():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert not wordBreak(s, wordDict)


def test_case_4():
    s = "bb"
    wordDict = ["a", "b", "bbb", "bbbb"]
    assert wordBreak(s, wordDict)


def test_case_5():
    s = "aaaaaaa"
    wordDict = ["aaa", "aaaa"]
    assert wordBreak(s, wordDict)

def test_lengths_1():
    lngths = [True, False, False, True, False]
    pos = 4
    r = [5, 4, 1]
    assert find_all_lengths(lngths, pos, max_len=20) == r

def test_lengths_2():
    lngths = [False, False, False, False, False]
    pos = 0
    r = [1]
    assert find_all_lengths(lngths, pos, max_len=20) == r
