from longest_valid_parentheses.app import longestValidParentheses


def test_case_1():
    s = "(()"
    c = 2
    assert longestValidParentheses(s) == c

def test_case_2():
    s = ")()())"
    c = 4
    assert longestValidParentheses(s) == c

def test_case_3():
    s = ""
    c = 0
    assert longestValidParentheses(s) == c

def test_case_4():
    s = "()(()"
    c = 2
    assert longestValidParentheses(s) == c


def test_case_5():
    s = "(()(((()"
    c = 2
    assert longestValidParentheses(s) == c


def test_case_6():
    s = "(()()"
    c = 4
    assert longestValidParentheses(s) == c