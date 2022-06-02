from ARRAY.string_has_codes.app import hasAllCodes


def test_case_1():
    s = "00110110"
    k = 2
    assert hasAllCodes(s, k)


def test_case_2():
    s = "0110"
    k = 1
    assert hasAllCodes(s, k)


def test_case_3():
    s = "0110"
    k = 2
    assert not hasAllCodes(s, k)


def test_case_4():
    s = "00110"
    k = 2
    assert hasAllCodes(s, k)
