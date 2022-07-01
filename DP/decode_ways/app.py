###########################################################################################
# leetcode problem  https://leetcode.com/problems/decode-ways/
###########################################################################################
from typing import Optional
from functools import lru_cache


def numDecodings(s: str) -> int:
    @lru_cache(None)
    def dfs(s: str) -> Optional[int]:
        if len(s) == 0:
            return 1   # because everything is correct we can count this

        if len(s) == 1:
            if s == "0":
                return 0
            else:
                return 1

        result = 0
        if "1" <= s[:2] <= "26":
            result += dfs(s[2:])
        if s[0] != "0":
            result += dfs(s[1:])

        return result

    return dfs(s)

