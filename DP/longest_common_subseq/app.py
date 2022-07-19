###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-common-subsequence/
###########################################################################################

def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for i, c1 in enumerate(text2):
        for j, c2 in enumerate(text1):
            if c1 == c2:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]
