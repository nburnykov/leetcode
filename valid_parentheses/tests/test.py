from valid_parentheses.app import isValid


def test_case_1():
    s = "()"
    assert isValid(s)

def test_case_2():
    s = "()[]{}"
    assert isValid(s)

def test_case_3():
    s = "(]{}"
    assert not isValid(s)
