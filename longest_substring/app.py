###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-substring-without-repeating-characters/
###########################################################################################

def lengthOfLongestSubstring2(s: str) -> int:
    if len(s) == 0:  # edge case
        return 0

    pointer_1 = 0
    pointer_2 = 0
    charset = set()
    max_len = 0
    while pointer_1 < len(s):
        if s[pointer_1] not in charset:
            charset.add(s[pointer_1])
            if len(charset) > max_len:
                max_len = len(charset)
        else:
            while s[pointer_2] != s[pointer_1]:
                charset.remove(s[pointer_2])
                pointer_2 += 1
            if pointer_2 < pointer_1:
                pointer_2 += 1
        pointer_1 += 1

    return max_len


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    cache = set()
    p1, p2, result = 0, 0, 0

    while p1 < len(s):
        if s[p1] not in cache:
            cache.add(s[p1])
            result = max(result, len(cache))
            p1 += 1
        else:
            cache.remove(s[p2])
            p2 += 1

    return result























