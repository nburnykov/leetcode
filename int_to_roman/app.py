###########################################################################################
# leetcode problem https://leetcode.com/problems/integer-to-roman/
###########################################################################################

def intToRoman(num: int) -> str:
    rome_map = {(0, 1): 'I', (0, 5): 'V', (1, 1): 'X', (1, 5): 'L', (2, 1): 'C', (2, 5): 'D', (3, 1): 'M'}
    result = []
    p = 0
    while num > 0:

        if p == 3:
            result.append('M' * num)
            break

        d = num % 10
        num //= 10

        if 0 < d < 4:
            result.append(rome_map[(p, 1)] * d)
        elif d == 4:
            result.append(rome_map[(p, 1)] + rome_map[(p, 5)])
        elif d == 5:
            result.append(rome_map[(p, 5)])
        elif 5 < d < 9:
            result.append(rome_map[(p, 5)] + rome_map[(p, 1)] * (d - 5))
        elif d == 9:
            result.append(rome_map[(p, 1)] + rome_map[(p + 1, 1)])

        p += 1

    return "".join(result[::-1])
