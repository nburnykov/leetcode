import unittest

from FSM.wildcard_match.app import fsm, isMatch


class TestApp(unittest.TestCase):
    def test_fsm_1(self):
        pattern = 'a*b?'
        fsm_ = {(-1, 'a'): {0}, (0, 'b'): {2}, (0, '?'): {1}, (1, '?'): {1}, (1, 'b'): {2}, (2, '?'): {3}}
        fs = {3}
        self.assertEqual(fsm(pattern), (fsm_, fs))

    def test_match_1(self):
        s = "aa"
        p = "a"
        self.assertFalse(isMatch(s, p))

    def test_match_2(self):
        s = "aa"
        p = "*"
        self.assertTrue(isMatch(s, p))

    def test_match_3(self):
        s = "cb"
        p = "?a"
        self.assertFalse(isMatch(s, p))


    def test_match_4(self):
        s = "cbccca"
        p = "?b*a"
        self.assertTrue(isMatch(s, p))

    def test_match_5(self):
        s = ""
        p = "*****"
        self.assertTrue(isMatch(s, p))

    def test_match_6(self):
        s = ""
        p = "abc"
        self.assertFalse(isMatch(s, p))