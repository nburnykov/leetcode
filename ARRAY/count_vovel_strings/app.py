###########################################################################################
# leetcode problem https://leetcode.com/problems/count-sorted-vowel-strings/
###########################################################################################

def countVowelStrings(n: int) -> int:
    """
    https://www.mathsisfun.com/combinatorics/combinations-permutations.html
    number of combinations with repetition
    (n+k-1)!/k!(n-1)! = (5+k-1)!/k!4! = (k+4)(k+3)(k+2)(k+1)/24
    """
    return round((n + 4) * (n + 3) * (n + 2) * (n + 1)) / 24
