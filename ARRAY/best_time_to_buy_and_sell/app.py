# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


def maxProfitMy(prices: List[int]) -> int:
    max_prices = []
    max_price = float("-inf")

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
            max_prices.append((i, max_price))

    max_profit = 0
    for i in range(len(prices) - 1):
        if max_prices[-1][0] < i:
            max_prices.pop(-1)
        max_profit = max(max_profit, max_prices[-1][1] - prices[i])

    return max_profit


def maxProfit(prices: List[int]) -> int:
    min_price, profit = float("inf"), 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)

    return profit
