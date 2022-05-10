import unittest

from FSM.re_match.app import fsm, isMatch


class TestApp(unittest.TestCase):
    def test_fsm_1(self):
        pattern = 'ab.c*d.*'
        fsm_ = {(-1, 'a'): {0}, (0, 'b'): {1}, (1, '.'): {2}, (2, 'c'): {3}, (2, 'd'): {4}, (3, 'c'): {3},
                (3, 'd'): {4}, (4, '.'): {5}, (5, '.'): {5}}
        fs = {4, 5}

        self.assertEqual(fsm(pattern), (fsm_, fs))

    def test_fsm_2(self):
        pattern = 'a*'
        fsm_ = {(-1, 'a'): {0}, (0, 'a'): {0}}
        fs = {0}

        self.assertEqual(fsm(pattern), (fsm_, fs))

    def test_fsm_3(self):
        pattern = ''
        fsm_ = {}
        fs = set()

        self.assertEqual(fsm(pattern), (fsm_, fs))

    def test_fsm_4(self):
        pattern = 'ab*a*.'
        fsm_ = {(-1, 'a'): {0}, (0, 'b'): {1}, (1, 'b'): {1}, (0, 'a'): {2}, (0, '.'): {3}, (1, 'a'): {2},
                (2, 'a'): {2}, (1, '.'): {3}, (2, '.'): {3}}
        fs = {3}

        self.assertEqual(fsm(pattern), (fsm_, fs))

    def test_match_1(self):
        s = "aa"
        p = "a"
        self.assertFalse(isMatch(s, p))

    def test_match_2(self):
        s = "aa"
        p = "a*"
        self.assertTrue(isMatch(s, p))

    def test_match_3(self):
        s = "aabc"
        p = ".*"
        self.assertTrue(isMatch(s, p))

    def test_match_4(self):
        s = "aab"
        p = "c*a*b"
        self.assertTrue(isMatch(s, p))

    def test_match_5(self):
        s = "ab"
        p = ".*c"
        self.assertFalse(isMatch(s, p))

    def test_match_6(self):
        s = "aaa"
        p = "a*a"
        self.assertTrue(isMatch(s, p))

    def test_match_7(self):
        s = "baabbbaccbccacacc"
        p = "c*..b*a*a.*a..*c"

        self.assertTrue(isMatch(s, p))

    def test_match_8(self):
        s = "baabbbaccbccacacc"
        p = "c*..b*a*a.*a..*c"

        self.assertTrue(isMatch(s, p))
