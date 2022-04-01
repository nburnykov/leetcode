from two_sum_2.two_sum_2 import twoSum


def test_case_1():
    numbers = [2, 7, 11, 15]
    target = 9
    output = [1, 2]
    assert twoSum(numbers, target) == output


def test_case_2():
    numbers = [2, 3, 4]
    target = 6
    output = [1, 3]
    assert twoSum(numbers, target) == output


def test_case_3():
    numbers = [-1, 0]
    target = -1
    output = [1, 2]
    assert twoSum(numbers, target) == output


def test_case_4():
    numbers = [5, 25, 75]
    target = 100
    output = [2, 3]
    assert twoSum(numbers, target) == output


def test_case_5():
    numbers = [3, 24, 50, 79, 88, 150, 345]
    target = 200
    output = [3, 6]
    assert twoSum(numbers, target) == output
