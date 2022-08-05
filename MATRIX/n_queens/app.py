from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    """
    The basic concept is that every single row can be occupied with only one queen, n rows = n queens
    we pass every row and choose the appropriate place for the next queen
    we do not need to store full queen coordinates, only their cols, because the position of column in the list itself
    is the corresponding row
    """
    def dfs(cols: list, diag_p: list, diag_s: list, n) -> list:
        row = len(cols)
        result = []

        if row == n:  # all cols placed
            return [cols]

        for c in range(n):  # loop through all possible cols

            dp = row + c   # figures placed on the principal diagonal have the same sum of row and column
            ds = row - c   # figures placed on the second diagonal have the same diff of row and column

            if c not in cols and dp not in diag_p and ds not in diag_s:  # place check
                result.extend(dfs(cols + [c], diag_p + [dp], diag_s + [ds], n))

        return result

    dfs_res = dfs([], [], [], n)
    formatted_res = []

    for r in dfs_res:
        strs = []

        for i in r:
            row = ['.'] * n
            row[i] = 'Q'
            strs.append("".join(row))

        formatted_res.append(strs)

    return formatted_res
