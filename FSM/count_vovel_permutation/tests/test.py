from FSM.count_vovel_permutation.app import countVowelPermutation


def test_case_1():
    n = 1
    r = 5
    assert countVowelPermutation(n) == r


def test_case_2():
    n = 2
    r = 10
    assert countVowelPermutation(n) == r


def test_case_3():
    n = 5
    r = 68
    assert countVowelPermutation(n) == r


def test_case_6():
    n = 144
    r = 18208803
    assert countVowelPermutation(n) == r