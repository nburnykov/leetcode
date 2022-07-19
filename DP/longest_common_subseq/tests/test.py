from DP.longest_common_subseq.app import longestCommonSubsequence


def test_case_1():
    text1 = "abcde"
    text2 = "ace"
    r = 3
    assert longestCommonSubsequence(text1, text2) == r

def test_case_2():
    text1 = "abc"
    text2 = "ac"
    r = 2
    assert longestCommonSubsequence(text1, text2) == r

def test_case_3():
    text1 = "abc"
    text2 = "def"
    r = 0
    assert longestCommonSubsequence(text1, text2) == r

def test_case_4():
    text1 = "ezupkr"
    text2 = "ubmrapg"
    r = 2
    assert longestCommonSubsequence(text1, text2) == r

def test_case_5():
    text1 = "oxcpqrsvwf"
    text2 = "shmtulqrypy"
    r = 2
    assert longestCommonSubsequence(text1, text2) == r
