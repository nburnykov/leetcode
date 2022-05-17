from divide_two_integers.app import divide


def test_case_1():
    dividend = 10
    divisor = 3
    r = 3
    assert divide(dividend, divisor) == r

def test_case_2():
    dividend = 7
    divisor = -3
    r = -2
    assert divide(dividend, divisor) == r