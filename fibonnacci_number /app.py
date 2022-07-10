###########################################################################################
# leetcode problem  https://leetcode.com/problems/fibonacci-number/
###########################################################################################

def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)