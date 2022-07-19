from DP.delete_two_strings.app import minDistance


def test_case_1():
    word1 = "sea"
    word2 = "eat"
    r = 2
    assert minDistance(word1, word2) == r


def test_case_2():
    word1 = "leetcode"
    word2 = "etco"
    r = 4
    assert minDistance(word1, word2) == r