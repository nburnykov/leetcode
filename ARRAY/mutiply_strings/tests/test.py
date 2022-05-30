from ARRAY.mutiply_strings.app import multiply


def test_case_1():
    a = '111'
    b = '252'
    r = '27972'
    assert multiply(b, a) == r

def test_case_2():
    a = '0'
    b = '0'
    r = '0'
    assert multiply(b, a) == r


def test_case_3():
    a = '9999'
    b = '9999'
    r = '99980001'
    assert multiply(b, a) == r

def test_case_4():
    a = '5'
    b = '5'
    r = '25'
    assert multiply(b, a) == r