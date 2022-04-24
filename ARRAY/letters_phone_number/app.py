###########################################################################################
# leetcode problem https://leetcode.com/problems/letter-combinations-of-a-phone-number/
###########################################################################################

from typing import List


def letterCombinations(digits: str) -> List[str]:
    def recursion(digits, index, letters):
        digit = int(digits[index])
        if index == len(digits) - 1:
            return list(letters[digit-2])
        else:
            result = []
            rec = recursion(digits, index + 1, letters)
            for l1 in list(letters[digit - 2]):
                for l2 in rec:
                    result.append(l1 + l2)
            return result

    letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    if len(digits) == 0:  # corner case
        return []

    return recursion(digits, 0, letters)
