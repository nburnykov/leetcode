###########################################################################################
# leetcode problem https://leetcode.com/problems/string-to-integer-atoi/
###########################################################################################

def myAtoi(s: str) -> int:
    s = s.strip()

    if len(s) == 0:  # corner case
        return 0

    sign = 1
    pointer = 0
    if s[0] == '-':
        sign = -1
        pointer = 1
    if s[0] == '+':
        pointer = 1

    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    for l in range(pointer, len(s)):
        c = digits.get(s[l])
        if c is None:
            break
        result = result * 10 + c

    max = 2 ** 31

    result *= sign
    result = -max if result < -max else result
    result = max - 1 if result > max - 1 else result

    return result
