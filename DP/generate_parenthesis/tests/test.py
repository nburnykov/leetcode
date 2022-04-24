from DP.generate_parenthesis.app import generateParenthesis


def test_case_1():
    n = 3
    r = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print(generateParenthesis(n))
    assert set(generateParenthesis(n)) == set(r)


def test_case_2():
    n = 4
    r = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
         "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
    print(set(r) - set(generateParenthesis(n)))


def test_case_3():
    n = 8
    print(len(generateParenthesis(n)))

    # assert set(generateParenthesis(n)) == set(r)
