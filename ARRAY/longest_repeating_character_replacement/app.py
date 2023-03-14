# https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(s: str, k: int) -> int:
    """
        we can find max in occurrences every time we change the sliding window
        max char variants 26 so O(max(0..26)) = O(1)
        overall complexity will be O(n)
    """
    char_occurrences = {}
    max_substr_len = 0
    l = r = 0
    max_char = 0
    while r < len(s):
        char_occurrences[s[r]] = char_occurrences.get(s[r], 0) + 1
        max_char = max(max_char, max(char_occurrences.values()))
        if r - l + 1 > max_char + k:
            char_occurrences[s[l]] = max(0, char_occurrences.get(s[l], 0) - 1)
            l += 1
        r += 1
        max_substr_len = max(max_substr_len, r - l)

    return max_substr_len
