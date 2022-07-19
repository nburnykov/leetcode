###########################################################################################
# leetcode problem  https://leetcode.com/problems/delete-operation-for-two-strings/
###########################################################################################

def minDistance(word1: str, word2: str) -> int:
    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
    for i, c1 in enumerate(word2):
        for j, c2 in enumerate(word1):
            if c1 == c2:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return len(word1) + len(word2) - 2 * dp[-1][-1]
