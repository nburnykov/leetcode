from DP.house_robber.house_robber import rob


def test_case_1():
    input = [1,2,3,1]
    output = 4
    assert rob(input) == output

def test_case_2():
    input = [2,7,9,3,1]
    output = 12
    assert rob(input) == output