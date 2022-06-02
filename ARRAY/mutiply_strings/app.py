###########################################################################################
# leetcode problem https://leetcode.com/problems/multiply-strings/
###########################################################################################

def multiply(num1: str, num2: str) -> str:
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    num_1_l = list(reversed(num1))
    num_2_l = list(reversed(num2))

    mults = []
    for i, n2 in enumerate(num_2_l):
        carriage = 0
        result = []
        for n1 in num_1_l:
            mult = int(n1) * int(n2) + carriage
            carriage = mult // 10
            result.append(mult % 10)
        result.append(carriage)
        mults.append([0] * i + result + [0] * (len(num_2_l) - i))

    result = []
    carriage = 0
    for i in range(len(mults[0])):
        r = 0
        for j in range(len(mults)):
            r += mults[j][i]
        r += carriage
        result.append(r % 10)
        carriage = r // 10

    carriage = '' if carriage==0 else str(carriage)

    result = (carriage + ''.join(map(str, result[::-1]))).lstrip('0')

    return result if len(result) > 0 else '0'





