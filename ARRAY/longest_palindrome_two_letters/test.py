from ARRAY.longest_palindrome_two_letters.app import longestPalindrome


def test_case_1():
    words = ["lc", "cl", "gg"]
    result = 6
    assert longestPalindrome(words) == result


def test_case_2():
    words = ["ab","ty","yt","lc","cl","ab"]
    result = 8
    assert longestPalindrome(words) == result


def test_case_3():
    words = ["cc","ll","xx"]
    result = 2
    assert longestPalindrome(words) == result


def test_case_4():
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    result = 22
    assert longestPalindrome(words) == result