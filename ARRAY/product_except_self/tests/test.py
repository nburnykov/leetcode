from ARRAY.product_except_self.app import productExceptSelf


def test_case_1():
    nums = [1, 2, 3, 4]
    r = [24, 12, 8, 6]
    assert productExceptSelf(nums) == r


def test_case_2():
    nums = [-1, 1, 0, -3, 3]
    r = [0, 0, 9, 0, 0]
    assert productExceptSelf(nums) == r

def test_case_3():
    nums = [0]
    r = [0]
    assert productExceptSelf(nums) == r


def test_case_4():
    nums = [0, 0, 0, 0, 0]
    r = [0, 0, 0, 0, 0]
    assert productExceptSelf(nums) == r


def test_case_5():
    nums = [0,4,0]
    r = [0, 0, 0]
    assert productExceptSelf(nums) == r

def test_case_6():
    nums = [0, 0]
    r = [0, 0]
    assert productExceptSelf(nums) == r