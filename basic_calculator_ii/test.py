from basic_calculator_ii.app import calculate


def test_case_1():
    s = "2 *  3 * 10 / 2 + 18 - 115 * 2"
    assert calculate(s) == -182

def test_case_2():
    s = "2"
    assert calculate(s) == 2


def test_case_3():
    s = "14-3/2"
    assert calculate(s) == 13