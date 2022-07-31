from functools import lru_cache
from typing import List, Optional


def coinChange(coins: List[int], amount: int) -> int:
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
