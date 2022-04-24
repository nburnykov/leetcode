from DFS_BFS.combination_sum.app import combinationSum


def test_case_1():
    candidates = [2, 3, 6, 7]
    target = 7
    result = [[2, 2, 3], [7]]
    assert combinationSum(candidates, target) == result


def test_case_2():
    candidates = [2, 3, 5]
    target = 8
    result = [[2,2,2,2],[2,3,3],[3,5]]
    assert combinationSum(candidates, target) == result

def test_case_3():
    candidates = []
    target = 0
    result = [[]]
    assert combinationSum(candidates, target) == result