###########################################################################################
# leetcode problem  https://leetcode.com/problems/add-strings/submissions/
###########################################################################################

def addStrings(num1: str, num2: str) -> str:
    result = ""

    remainder = 0
    for i in range(max(len(num1), len(num2))):
        n1 = int(num1[~i]) if i < len(num1) else 0
        n2 = int(num2[~i]) if i < len(num2) else 0

        s = n2 + n1 + remainder

        result = str(s % 10) + result
        remainder = s // 10

    if remainder > 0:
        result = remainder + result

    return result
