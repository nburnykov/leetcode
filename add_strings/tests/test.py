from add_strings.app import addStrings


def test_case_1():
    num1 = "11"
    num2 = "123"
    r = "134"
    assert addStrings(num1, num2) == r


def test_case_2():
    num1 = "456"
    num2 = "77"
    r = "533"
    assert addStrings(num1, num2) == r


def test_case_3():
    num1 = "0"
    num2 = "0"
    r = "0"
    assert addStrings(num1, num2) == r