from DFS_BFS.combination_sum_2.app import combinationSum2


def test_case_1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    assert combinationSum2(candidates, target) == result


def test_case_2():
    candidates = [2,5,2,1,2]
    target = 5
    result = [
        [1, 2, 2],
        [5]
    ]
    assert combinationSum2(candidates, target) == result