from sorted_squares.app import sortedSquares


def test_case_1():
    nums = [-4, -1, 0, 3, 10]
    output = [0, 1, 9, 16, 100]
    assert sortedSquares(nums) == output


def test_case_2():
    nums = [-1]
    output = [1]
    assert sortedSquares(nums) == output