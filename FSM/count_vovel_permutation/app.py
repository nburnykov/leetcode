###########################################################################################
# leetcode problem  https://leetcode.com/problems/count-vowels-permutation/
###########################################################################################

def countVowelPermutation_slow(n: int) -> int:
    """
    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.
    """
    fsm = {
        'a': ['e'],
        'e': ['a', 'i'],
        'i': ['a', 'e', 'o', 'u'],
        'o': ['i', 'u'],
        'u': ['a'],
    }
    counters = {(k, 1): 1 for k in fsm.keys()}

    for i in range(1, n):
        for vowel, nxt_v in fsm.items():
            counters[(vowel, i + 1)] = sum([counters[(nv, i)] for nv in nxt_v])
        for vowel in fsm.keys():  # memory opt
            counters.pop((vowel, i))

    return sum([counters[(k, n)] for k in fsm.keys()]) % (10 ** 9 + 7)


def countVowelPermutation(n: int) -> int:
    dp = [1] * 5
    for _ in range(n - 1):
        a, e, i, o, u = dp
        dp[0] = e
        dp[1] = a + i
        dp[2] = a + e + o + u
        dp[3] = i + u
        dp[4] = a

    return sum(dp) % (10 ** 9 + 7)
