def lengthOfLongestSubstring(s: str) -> int:
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
