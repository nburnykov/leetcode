import unittest

from ARRAY.count_vovel_strings.app import countVowelStrings


class TestApp(unittest.TestCase):
    def test_case_1(self):
        n = 1
        self.assertEqual(countVowelStrings(n), 5)

    def test_case_2(self):
        n = 2
        self.assertEqual(countVowelStrings(n), 15)

    def test_case_3(self):
        n = 33
        self.assertEqual(countVowelStrings(n), 66045)
