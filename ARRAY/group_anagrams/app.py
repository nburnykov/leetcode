###########################################################################################
# leetcode problem https://leetcode.com/problems/group-anagrams/
###########################################################################################

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = dict()
    for s in strs:
        anagrams.setdefault(tuple(sorted(s)), []).append(s)
    return list(anagrams.values())