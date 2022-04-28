from DP.house_robber_2.app import rob


def test_case_1():
    nums = [2, 3, 2]
    r = 3
    assert rob(nums) == r

def test_case_2():
    nums = [1,2,3,1]
    r = 4
    assert rob(nums) == r

def test_case_3():
    nums = [1, 2, 3]
    r = 3
    assert rob(nums) == r

def test_case_4():
    nums = [200,3,140,20,10]
    r = 340
    assert rob(nums) == r

def test_case_5():
    nums = [1,3,1,3,100]
    r = 103
    assert rob(nums) == r
