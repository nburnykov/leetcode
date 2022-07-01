from DP.unique_paths_2.app import uniquePathsWithObstacles


def test_case_1():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    r = 2
    assert uniquePathsWithObstacles(obstacleGrid) == r

def test_case_2():
    obstacleGrid = [[0,1],[0,0]]
    r = 1
    assert uniquePathsWithObstacles(obstacleGrid) == r