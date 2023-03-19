# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List


def maxProfit(prices: List[int]) -> int:
    rested, bought, sold = 0, float("-inf"), float("-inf")
    for p in prices:
        rested_new = max(rested, sold)
        bought_new = max(bought, rested - p)
        sold = bought + p
        rested, bought = rested_new, bought_new

    return max(rested, sold)


def maxProfit2(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    rested = [0] * len(prices)
    bought = [0] * len(prices)
    sold = [0] * len(prices)
    rested[0] = 0
    bought[0] = -prices[0]
    sold[0] = float("-inf")

    for i in range(1, len(prices)):
        rested[i] = max(rested[i - 1], sold[i - 1])
        bought[i] = max(bought[i - 1], rested[i - 1] - prices[i])
        sold[i] = bought[i - 1] + prices[i]

    return max(rested[-1], sold[-1])
