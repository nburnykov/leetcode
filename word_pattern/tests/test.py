from word_pattern.app import wordPattern


def test_case_1():
    pattern = "abba"
    s = "dog cat cat dog"
    assert wordPattern(pattern, s)


def test_case_2():
    pattern = "abba"
    s = "dog cat cat fish"
    assert not wordPattern(pattern, s)


def test_case_3():
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert not wordPattern(pattern, s)


def test_case_4():
    pattern = "abba"
    s = "dog dog dog dog"
    assert not wordPattern(pattern, s)
