###########################################################################################
# leetcode problem  https://leetcode.com/problems/integer-break/
###########################################################################################

def integerBreak(n: int) -> int:
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4

    comp = n // 3
    rem = n % 3

    if rem < 2:
        return 3 ** (comp - 1) * (rem + 3)
    else:
        return 3 ** comp * rem
