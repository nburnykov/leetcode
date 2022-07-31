from functools import lru_cache


@lru_cache(None)
def minDistance(word1: str, word2: str) -> int:
    """
    Levenshtein distance
    lev(a, b) =
        |a| if b = 0,
        |b| if a = 0,
        lev(a[1:], b[1:]) if a[0] = b[0]   # in case of equal first char
        1 + min(lev(a, b[1:]), lev(b, a[:1]), lev(a[:1], b[:1])) if a[0] != b[0]  # in case of unequal first char

    Recursive approach
    """
    if len(word2) == 0:
        return len(word1)
    if len(word1) == 0:
        return len(word2)

    if word1[0] == word2[0]:
        return minDistance(word1[1:], word2[1:])
    else:
        return 1 + min(minDistance(word1[1:], word2), minDistance(word1, word2[1:]), minDistance(word1[1:], word2[1:]))



