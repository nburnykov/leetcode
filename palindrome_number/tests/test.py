import unittest

from palindrome_number.app import isPalindrome


class TestApp(unittest.TestCase):
    def test_case_1(self):
        i = 121
        self.assertTrue(isPalindrome(i))

    def test_case_2(self):
        i = -121
        self.assertFalse(isPalindrome(i))
