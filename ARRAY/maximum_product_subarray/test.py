from ARRAY.maximum_product_subarray.app import maxProduct


def test_case_1():
    nums = [2, 3, -2, 4]
    r = 6
    assert maxProduct(nums) == r

def test_case_2():
    nums = [-2, 0, -1]
    r = 0
    assert maxProduct(nums) == r

def test_case_3():
    nums = [2, 3, -2, 4]
    r = 6
    assert maxProduct(nums) == r