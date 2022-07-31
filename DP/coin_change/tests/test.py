from DP.coin_change.app import coinChange


def test_case_1():
    coins = [1, 2, 5]
    amount = 11
    r = 3
    assert coinChange(coins, amount) == r

def test_case_2():
    coins = [2]
    amount = 3
    r = -1
    assert coinChange(coins, amount) == r