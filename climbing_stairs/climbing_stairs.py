###########################################################################################
# leetcode problem https://leetcode.com/problems/climbing-stairs/
###########################################################################################
from math import comb


def climbStairs(n: int) -> int:
    result = 0
    for i in range(n // 2 + 1):
        result += comb(n - i, i)
    return result