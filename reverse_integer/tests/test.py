import unittest

from reverse_integer.app import reverse


class TestApp(unittest.TestCase):
    def test_case_1(self):
        i = 12345
        r = 54321
        self.assertEqual(reverse(i), r)

    def test_case_2(self):
        i = 0
        r = 0
        self.assertEqual(reverse(i), r)