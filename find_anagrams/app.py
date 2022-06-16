###########################################################################################
# leetcode problem https://leetcode.com/problems/find-all-anagrams-in-a-string
###########################################################################################

from typing import List


def findAnagrams(s: str, p: str) -> List[int]:  # true O(n) solution
    result = []

    hash = dict()
    for l in p:
        hash[l] = hash.get(l, 0) + 1

    cache = dict()
    for i_insert in range(len(s)):

        i_remove = i_insert - len(p)
        l_remove = s[i_remove] if i_remove >= 0 else None
        if l_remove is not None:
            cache[l_remove] = cache.get(l_remove, 0) - 1
            if cache[l_remove] == 0:
                cache.pop(l_remove)

        l_insert = s[i_insert]
        cache[l_insert] = cache.get(l_insert, 0) + 1

        if hash == cache:
            result.append(i_insert - len(p) + 1)

    return result
