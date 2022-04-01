from longest_substring.longest_substring import lengthOfLongestSubstring


def test_case_1():
    input = "abcabcbb"
    output = 3
    assert lengthOfLongestSubstring(input) == output


def test_case_2():
    input = "bbbbb"
    output = 1
    assert lengthOfLongestSubstring(input) == output


def test_case_3():
    input = "pwwkew"
    output = 3
    assert lengthOfLongestSubstring(input) == output
