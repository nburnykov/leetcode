###########################################################################################
# leetcode problem https://leetcode.com/problems/reverse-integer/
###########################################################################################

def reverse(x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1

    absx = abs(x)
    result = 0
    while absx > 0:
        digit = absx % 10
        absx //= 10
        result = result * 10 + digit

    max = 2 ** 31

    return result * sign if -max <= result <= max else 0