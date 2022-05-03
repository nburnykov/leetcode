###########################################################################################
# leetcode problem https://leetcode.com/problems/longest-palindromic-substring/
###########################################################################################


def longestPalindrome(s: str) -> str:
    def check_palindrome(substr: str) -> str:
        if len(substr) < 2:  # corner cases
            return substr

        if len(substr) % 2:
            c = 1
        else:
            c = 0
        middle = len(substr) // 2
        i0, i1 = middle - 1, middle + c
        is_found = False
        while substr[i0] == substr[i1]:
            is_found = True
            i0 -= 1
            i1 += 1
            if i0 == -1:
                break

        return substr[i0+1:i1] if is_found else ''

    longest_palindrome = ''
    for i in range(len(s) + 1):
        palindrome = check_palindrome(s[:i])
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

    for i in range(len(s), -1, -1):
        palindrome = check_palindrome(s[i:])
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

    return longest_palindrome
