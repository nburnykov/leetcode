###########################################################################################
# leetcode problem https://leetcode.com/problems/backspace-string-compare/
###########################################################################################
from typing import Optional


def backspaceCompare(s: str, t: str) -> bool:  # O(n) time complexity and O(1) space complexity

    def _next_i(string, i) -> Optional[int]:
        count = 0
        while i >= 0:
            count = count + 1 if string[i] == '#' else count - 1
            if count > -1:
                i -= 1
            else:
                return i

    # corner cases
    if not s and not t:
        return True
    if len(s) == len(t) == 1:
        return s == t

    i, j = len(s) - 1, len(t) - 1
    result = True
    while result:
        i, j = _next_i(s, i), _next_i(t, j)
        if i is None and j is None:
            return True
        if i is None or j is None:
            return False
        result = s[i] == t[j]
        i -= 1
        j -= 1
    return result
