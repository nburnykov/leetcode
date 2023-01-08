###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
###########################################################################################

from typing import List


def longestPalindrome(words: List[str]) -> int:
    word_map = dict()
    has_symmetric_word = False
    for w in words:
        sw = tuple(sorted(w))
        if sw[0] == sw[1]:
            word_map[sw[0]] = word_map.get(sw[0], 0) + 1
        if sw in word_map:
            if sw == tuple(w):
                word_map[sw][0] += 1
            else:
                word_map[sw][1] += 1
        else:
            if sw == tuple(w):
                word_map[sw] = [1, 0]
            else:
                word_map[sw] = [0, 1]

    s = 0
    for k, v in word_map.items():
        if len(k) == 2:
            s += 2 * min(v)
        else:
            has_symmetric_word = has_symmetric_word or v % 2
            s += 2 * (v // 2)

    s += has_symmetric_word

    return s * 2

