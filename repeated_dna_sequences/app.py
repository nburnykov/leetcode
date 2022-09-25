###########################################################################################
# leetcode problem  https://leetcode.com/problems/repeated-dna-sequences/
###########################################################################################
from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    cache = dict()
    result = []
    i = 0
    while i < len(s) - 10 + 1:
        subs = s[i:i + 10]
        if cache.get(subs, 0) == 1:
            result.append(subs)
            cache[subs] += 1
        if subs not in cache:
            cache[subs] = 1
        i += 1

    return result


def findRepeatedDnaSequences1(s: str) -> List[str]:
    """
    rolling hash method
    """
    if len(s) < 10:
        return []

    PRIME_CONST = 50707
    SUBSEQ_LNG = 10

    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    ld = len(d)
    enc_s = [d[ch] for ch in s]

    hash = 0
    for i in range(SUBSEQ_LNG):
        hash += enc_s[i] * ld ** (SUBSEQ_LNG - i - 1)

    hash %= PRIME_CONST

    result = []
    cache = {hash: [[0, 1]]}
    for i in range(1, len(enc_s) - SUBSEQ_LNG + 1):
        code_left = enc_s[i - 1]
        code_new = enc_s[i + 9]
        hash = (hash - code_left * ld ** (SUBSEQ_LNG - 1)) * ld + code_new
        hash %= PRIME_CONST

        h = cache.get(hash, [])
        if len(h) == 0:
            cache[hash] = [[i, 1]]
        else:
            for j in range(len(h)):
                start = h[j][0]
                if enc_s[start: start + SUBSEQ_LNG] == enc_s[i: i + SUBSEQ_LNG]:
                    h[j][1] += 1
                    if h[j][1] == 2:
                        result.append(s[i: i + SUBSEQ_LNG])
                else:
                    cache[hash].append([i, 1])

    return result
