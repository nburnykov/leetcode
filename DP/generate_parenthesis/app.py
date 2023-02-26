###########################################################################################
# leetcode problem https://leetcode.com/problems/generate-parentheses/
###########################################################################################

from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = [[""]]
    for i in range(0, n):  # every next layer uses previous data i = last layer
        result.append([])
        for j in range(0, i + 1):
            for r1 in result[j]:  # iterate through j layer
                for r2 in result[i - j]: # addition
                    result[i + 1].append("(" + r1 + ")" + r2)
    return result[n]
