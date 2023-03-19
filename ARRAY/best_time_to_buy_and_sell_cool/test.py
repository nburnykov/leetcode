from ARRAY.best_time_to_buy_and_sell_cool.app import maxProfit


def test_case_1():
    prices = [1, 2, 3, 0, 2]
    result = 3
    assert maxProfit(prices) == result


def test_case_2():
    prices = [1]
    result = 0
    assert maxProfit(prices) == result


def test_case_3():
    prices = [2,1,2,0,1]
    result = 1
    assert maxProfit(prices) == result


def test_case_4():
    prices = [2,1,2,0,1]
    result = 1
    assert maxProfit(prices) == result