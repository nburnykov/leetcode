###########################################################################################
# leetcode problem  https://leetcode.com/problems/word-break/
###########################################################################################
from typing import List, Optional


def wordBreak2(s: str, wordDict: List[str]) -> bool:  # a slow solution using recursion

    def search(s, word_set) -> bool:
        w = ""
        if len(s) == 0:
            return True
        results = []
        for i, ch in enumerate(s):
            w += ch
            if w in word_set:
                results.append(search(s[i + 1:], word_set))
            if len(w) == 20:
                return any(results)

        return any(results)

    word_set = set(wordDict)
    return search(s, word_set)


def find_all_lengths(arr: List[bool], pos: int, max_len: Optional[int] = None) -> List[int]:
    result = []
    if max_len is not None:
        start = pos - max_len
        if start < 0:
            start = 0
            result.append(pos + 1)
    else:
        start = 0
    for i in range(start, pos + 1):
        ln = pos - i
        if arr[i] and ln > 0:
            result.append(ln)
    return result


def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    A DP approach
    """
    word_set = set(wordDict)
    results = [False] * len(s)
    for i in range(len(s)):
        lns = find_all_lengths(results, i, max_len=20)
        for l in lns:
            slice = s[i - l + 1:i + 1]
            if slice in word_set:
                results[i] = True
                break
    return results[-1]


