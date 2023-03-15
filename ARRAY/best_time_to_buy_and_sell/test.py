from ARRAY.best_time_to_buy_and_sell.app import maxProfit


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    result = 5
    assert maxProfit(prices) == result


def test_case_2():
    prices = [7,6,4,3,1]
    result = 0
    assert maxProfit(prices) == result