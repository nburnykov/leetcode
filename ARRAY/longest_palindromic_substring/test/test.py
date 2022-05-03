import unittest

from ARRAY.longest_palindromic_substring.app import longestPalindrome


class TestStringMethods(unittest.TestCase):
    def test_case_1(self):
        s = "babad"
        r = "bab"
        self.assertEqual(longestPalindrome(s), r)

    def test_case_2(self):
        s = "cbbd"
        r = "bb"
        self.assertEqual(longestPalindrome(s), r)

    def test_case_3(self):
        s = "c"
        r = "c"
        self.assertEqual(longestPalindrome(s), r)

    def test_case_4(self):
        s = "acbcdcbcm"
        r = "cbcdcbc"
        self.assertEqual(longestPalindrome(s), r)

    def test_case_5(self):
        s = "ac"
        r = "a"
        self.assertEqual(longestPalindrome(s), r)