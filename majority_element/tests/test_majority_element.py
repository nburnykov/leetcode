from majority_element.majority_element import majorityElement


def test_case_1():
    nums = [3, 2, 3]
    output = 3
    assert majorityElement(nums) == output


def test_case_2():
    nums = [6, 5, 5]
    output = 5
    assert majorityElement(nums) == output


