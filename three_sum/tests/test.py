from three_sum.app import threeSum


def test_case_1():
    input = [-1, 0, 1, 2, -1, -4]
    output = [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum(input) == output


def test_case_2():
    input = []
    output = []
    assert threeSum(input) == output


def test_case_3():
    input = [0]
    output = []
    assert threeSum(input) == output


def test_case_4():
    input = [0,0,0,0]
    output = [[0,0,0]]
    assert threeSum(input) == output