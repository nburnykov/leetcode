import unittest

from ARRAY.string_to_integer.app import myAtoi


class TestApp(unittest.TestCase):
    def test_case_1(self):
        s = "42"
        i = 42
        self.assertEqual(myAtoi(s), i)

    def test_case_2(self):
        s = "   -42"
        i = -42
        self.assertEqual(myAtoi(s), i)

    def test_case_3(self):
        s = "    4222a22with words"
        i = 4222
        self.assertEqual(myAtoi(s), i)