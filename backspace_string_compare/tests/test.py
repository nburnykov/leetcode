from backspace_string_compare.app import backspaceCompare


# def test_case_add_1():
#     enc_s = 'c#ba##'
#     assert next_i(enc_s, len(enc_s) - 1) is None
#
#
# def test_case_add_2():
#     enc_s = 'c#ba#'
#     assert next_i(enc_s, len(enc_s) - 1) == 2


def test_case_1():
    s = "ab#c"
    t = "ad#c"
    assert backspaceCompare(s, t)


def test_case_2():
    s = "ab##"
    t = "c#d#"
    assert backspaceCompare(s, t)


def test_case_3():
    s = "a#c"
    t = "b"
    assert not backspaceCompare(s, t)


def test_case_4():
    s = "#"
    t = "b"
    assert not backspaceCompare(s, t)


def test_case_5():
    s = "#####"
    t = ""
    assert backspaceCompare(s, t)
