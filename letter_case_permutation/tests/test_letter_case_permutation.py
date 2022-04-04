from letter_case_permutation.letter_case_permutation import letterCasePermutation


def test_case_1():
    s = "a1b2"
    out = ['a1b2', 'A1b2', 'a1B2', 'A1B2']
    assert set(letterCasePermutation(s)) == set(out)

def test_case_2():
    s = "C"
    out = ["c", "C"]
    assert set(letterCasePermutation(s)) == set(out)

def test_case_3():
    s = "mQe"
    out = ["mqe","mqE","mQe","mQE","Mqe","MqE","MQe","MQE"]
    assert set(letterCasePermutation(s)) == set(out)