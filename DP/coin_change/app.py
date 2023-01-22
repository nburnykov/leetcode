# https://leetcode.com/problems/coin-change
import functools
from collections import deque
from functools import lru_cache
from typing import List, Optional


def coinChange2(coins: List[int], amount: int) -> int:
    @lru_cache(None)
    def calc(amount_left: int) -> Optional[int]:
        if amount_left < 0:
            return
        if amount_left == 0:
            return 0
        result = []
        for c in coins:
            r = calc(amount_left - c)
            if r is not None:
                result.append(r + 1)

        return min(result) if len(result) > 0 else None

    r = calc(amount)
    return r if r is not None else -1


def coinChange1(coins: List[int], amount: int) -> int:
    @functools.lru_cache(None)
    def change(amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        result = []
        for c in coins:
            r = change(amount - c)
            if r != -1:
                result.append(r)

        if len(result) == 0:
            return -1
        else:
            return min(result) + 1

    return change(amount)


def coinChange(coins: List[int], amount: int) -> int:
    q = deque([(0, amount)])
    cached = {amount}
    while len(q) > 0:
        num_coins, amount = q.popleft()
        if amount == 0:
            return num_coins
        if amount < 0:
            continue

        for c in coins:
            if amount - c not in cached:
                q.append((num_coins + 1, amount - c))

    return -1
