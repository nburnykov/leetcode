from FSM.valid_number.app import isNumber


def test_case_1():
    s = "+3.14"
    assert isNumber(s)


def test_case_2():
    s = "0"
    assert isNumber(s)


def test_case_3():
    s = "e"
    assert not isNumber(s)


def test_case_4():
    s = "."
    assert not isNumber(s)


def test_case_5():
    s = "53.5e93"
    assert isNumber(s)


def test_case_6():
    s = "2e0"
    assert isNumber(s)


def test_case_7():
    s = "-."
    assert not isNumber(s)


def test_case_8():
    s = "46.e3"
    assert isNumber(s)


def test_case_9():
    s = ".e1"
    assert not isNumber(s)

def test_case_10():
    s = ".0e7"

    assert isNumber(s)