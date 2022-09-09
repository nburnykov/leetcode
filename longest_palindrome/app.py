###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-palindrome/
###########################################################################################

def longestPalindrome(s: str) -> int:
    strmap = {}
    add_one = 0
    ln = 0

    for n in s:
        strmap[n] = strmap.get(n, 0) + 1

    for _, cnt in strmap.items():
        rem = cnt % 2
        ln += cnt - rem
        if rem == 1:
            add_one = 1

    return ln + add_one