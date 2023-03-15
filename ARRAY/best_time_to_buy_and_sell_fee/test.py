from ARRAY.best_time_to_buy_and_sell_fee.app import maxProfit


def test_case_1():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    result = 8
    assert maxProfit(prices, fee) == result


def test_case_2():
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    result = 6
    assert maxProfit(prices, fee) == result


def test_case_3():
    prices = [9, 8, 7, 1, 2]
    fee = 3
    result = 0
    assert maxProfit(prices, fee) == result


def test_case_4():
    prices = [4,5,2,4,3,3,1,2,5,4]
    fee = 1
    result = 4
    assert maxProfit(prices, fee) == result