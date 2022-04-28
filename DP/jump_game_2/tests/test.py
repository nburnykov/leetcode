from DP.jump_game_2.app import jump


def test_case_1():
    nums = [2, 3, 1, 1, 4]
    r = 2
    assert jump(nums) == r

def test_case_2():
    nums = [2,3,0,1,4]
    r = 2
    assert jump(nums) == r
