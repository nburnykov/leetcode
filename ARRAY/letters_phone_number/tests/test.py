from ARRAY.letters_phone_number.app import letterCombinations


def test_case_1():
    digits = "23"
    result = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letterCombinations(digits) == result

def test_case_2():
    digits = ""
    result = []
    assert letterCombinations(digits) == result

def test_case_3():
    digits = "2"
    result = ['a', 'b', 'c']
    assert letterCombinations(digits) == result