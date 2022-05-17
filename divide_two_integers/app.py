###########################################################################################
# leetcode problem https://leetcode.com/problems/divide-two-integers/
###########################################################################################

def divide(dividend: int, divisor: int) -> int:
    a_div = abs(dividend)
    a_dvsr = abs(divisor)
    i = 0
    while a_div >= a_dvsr:
        temp_div = a_dvsr
        temp_i = 1
        while a_div >= temp_div:
            a_div -= temp_div
            i += temp_i
            temp_i *= 2
            temp_div *= 2

    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        i = -i

    return min(max(-2 ** 31, i), 2 ** 31 - 1)
