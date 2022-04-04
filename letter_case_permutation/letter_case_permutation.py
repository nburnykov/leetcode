###########################################################################################
# leetcode problem https://leetcode.com/problems/letter-case-permutation/
###########################################################################################

from typing import List


def letterCasePermutation(s: str) -> List[str]:
    char_list = list(s)
    char_indexes = []
    for i, c in enumerate(char_list):
        if c.isalpha():
            char_indexes.append(i)

    if len(char_indexes) == 0:
        return [s]

    result = []
    masks = [list(format(x, f'0{len(char_indexes)}b')) for x in range(2 ** len(char_indexes))]
    for m in masks:
        char_list_copy = char_list[:]
        for i, cm in enumerate(m):
            c = char_list_copy[char_indexes[i]]
            char_list_copy[char_indexes[i]] = c.upper() if int(cm) else c.lower()

        result.append("".join(char_list_copy))

    return result
