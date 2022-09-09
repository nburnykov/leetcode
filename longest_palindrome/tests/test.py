from longest_palindrome.app import longestPalindrome


def test_case_1():
    s = "abccccdd"
    r = 7
    assert longestPalindrome(s) == r


def test_case_2():
    s = "a"
    r = 1
    assert longestPalindrome(s) == r