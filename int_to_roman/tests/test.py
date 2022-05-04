import unittest

from int_to_roman.app import intToRoman


class TestApp(unittest.TestCase):
    def test_case_1(self):
        i = 54
        r = 'LIV'
        self.assertEqual(intToRoman(i), r)

    def test_case_2(self):
        i = 3
        r = 'III'
        self.assertEqual(intToRoman(i), r)

    def test_case_3(self):
        i = 584
        r = 'DLXXXIV'
        self.assertEqual(intToRoman(i), r)

    def test_case_4(self):
        i = 1983
        r = 'MCMLXXXIII'
        self.assertEqual(intToRoman(i), r)

    def test_case_5(self):
        i = 8500
        r = 'MMMMMMMMD'
        self.assertEqual(intToRoman(i), r)

