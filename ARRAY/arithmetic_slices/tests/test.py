from ARRAY.arithmetic_slices.app import numberOfArithmeticSlices


def test_case_1():
    nums = [1, 2, 3, 4]
    r = 3
    assert numberOfArithmeticSlices(nums) == r