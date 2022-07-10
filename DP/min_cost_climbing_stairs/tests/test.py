from DP.min_cost_climbing_stairs.app import minCostClimbingStairs


def test_case_1():
    cost = [10, 15, 20]
    r = 15
    assert minCostClimbingStairs(cost) == r


def test_case_2():
    cost = [1,100,1,1,1,100,1,1,100,1]
    r = 6
    assert minCostClimbingStairs(cost) == r