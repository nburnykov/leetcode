###########################################################################################
# leetcode problem  https://leetcode.com/problems/n-queens-ii/
###########################################################################################

def totalNQueens(n: int) -> int:
    """
    For the algo explanation see n_queens solution
    """
    def dfs(cols: list, diag_p: list, diag_s: list, n: int) -> int:
        result = 0
        row = len(cols)

        if len(cols) == n:
            return 1

        for c in range(n):
            diag_1 = row - c
            diag_2 = row + c

            if c not in cols and diag_1 not in diag_p and diag_2 not in diag_s:
                result += dfs(cols + [c], diag_p + [diag_1], diag_s + [diag_2], n)

        return result

    return dfs([], [], [], n)