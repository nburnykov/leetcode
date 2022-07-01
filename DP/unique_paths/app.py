###########################################################################################
# leetcode problem  https://leetcode.com/problems/unique-paths/
###########################################################################################

def uniquePaths(m: int, n: int) -> int:
    matrix = [[0] * n for _ in range(m)]
    for x in range(m - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if x + 1 > m - 1 or y + 1 > n - 1:
                matrix[x][y] = 1
                continue

            matrix[x][y] = matrix[x + 1][y] + matrix[x][y + 1]

    return matrix[0][0]