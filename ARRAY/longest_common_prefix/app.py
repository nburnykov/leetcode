###########################################################################################
# leetcode problem https://leetcode.com/problems/longest-common-prefix/
###########################################################################################
from typing import List


def longestCommonPrefix2(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    reference = strs[0]
    for string in strs:
        i = -1
        for i, e in enumerate(reference):
            if len(string) < i + 1 or string[i] != e:
                i -= 1
                break

        reference = reference[:i + 1]
        if len(reference) == 0:
            return ""

    return reference


def longestCommonPrefix(strs: List[str]) -> str:
    min_len = min([len(st) for st in strs])
    result = []
    for i in range(min_len):
        char_set = set()
        for st in strs:
            char_set.add(st[i])
        if len(char_set) == 1:
            result.append(char_set.pop())
        else:
            break
    return "".join(result)