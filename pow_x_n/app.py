###########################################################################################
# leetcode problem  https://leetcode.com/problems/powx-n/
###########################################################################################

def myPowSlow(x: float, n: int) -> float:
    """
    Direct way - time limit exceeded
    """

    if n == 0:
        return 1
    if x == 0:
        return 0

    if n < 0:
        pw = -n
    else:
        pw = n

    res = 1
    for _ in range(pw):
        res *= x

    return 1 / res if n < 0 else res


def myPow(x: float, n: int) -> float:
    """
    A faster approach
    https://www.rookieslab.com/posts/fast-power-algorithm-exponentiation-by-squaring-cpp-python-implementation
    """
    if x == 0:
        return 0
    if n == 0:
        return 1

    curr = x
    result = 1

    if n < 0:
        pow = -n
    else:
        pow = n

    while pow > 1:
        if pow % 2 == 1:
            result *= curr
            pow -= 1
        else:
            curr *= curr
            pow /= 2

    result *= curr

    return 1 / result if n < 0 else result