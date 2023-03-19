# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


def maxProfit2(prices: List[int], fee: int) -> int:
    profit = 0
    min_val, max_val = prices[0], prices[0]
    for i in range(1, len(prices)):
        max_val = max(prices[i], max_val)
        if prices[i] <= min_val and prices[i] >= max_val - fee:
            min_val, max_val = prices[i], prices[i]

        if prices[i] < max_val - fee or i == len(prices) - 1:
            profit += max(max_val - min_val - fee, 0)
            min_val, max_val = prices[i], prices[i]

    return profit


def maxProfit(prices: List[int], fee: int) -> int:
    bought = -prices[0] - fee
    sold = 0
    for p in prices[1:]:
        bought_new = max(bought, sold - p - fee)
        sold_new = max(sold, bought + p)
        bought, sold = bought_new, sold_new

    return max(bought, sold)
