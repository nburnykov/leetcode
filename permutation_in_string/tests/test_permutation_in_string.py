from permutation_in_string.permutation_in_string import checkInclusion


def test_case_1():
    s1 = "ab"
    s2 = "eidbaooo"
    assert checkInclusion(s1, s2)

def test_case_2():
    s1 = "ab"
    s2 = "eidboaoo"
    assert not checkInclusion(s1, s2)

def test_case_3():
    s1 = "adc"
    s2 = "dcda"
    assert checkInclusion(s1, s2)

def test_case_4():
    s1 = "hello"
    s2 = "ooolleoooleh"
    assert not checkInclusion(s1, s2)