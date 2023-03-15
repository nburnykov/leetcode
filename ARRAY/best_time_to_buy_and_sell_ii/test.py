from ARRAY.best_time_to_buy_and_sell_ii.app import maxProfit


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    result = 7
    assert maxProfit(prices) == result


def test_case_2():
    prices = [1, 2, 3, 4, 5]
    result = 4
    assert maxProfit(prices) == result


def test_case_3():
    prices = [7, 6, 4, 3, 1]
    result = 0
    assert maxProfit(prices) == result
