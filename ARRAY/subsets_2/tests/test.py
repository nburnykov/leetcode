from ARRAY.subsets_2.app import subsetsWithDup


def test_case_1():
    nums = [1, 2, 2]
    result = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    assert subsetsWithDup(nums) == result