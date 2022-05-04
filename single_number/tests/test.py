from single_number.app import singleNumber


def test_case_1():
    input = [1,2,3,5,3,2,1]
    output = 5
    assert singleNumber(input) == output