###########################################################################################
# leetcode problem https://leetcode.com/problems/01-matrix/
###########################################################################################

from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:

    def get_min(mtx, i, j):
        values = []
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:

            if 0 <= x < len(mtx) and 0 <= y < len(mtx[0]):
                values.append(mtx[x][y])

        return min(values) + 1

    if len(mat) == 0:
        return mat

    cells_to_reprocess = dict()
    result = [[None] * len(mat[0]) for _ in mat]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i][j] = 0 if not mat[i][j] else get_min(mat, i, j)
            if result[i][j] > 1:
                cells_to_reprocess.setdefault(result[i][j], set()).add((i, j))

    changed = True
    while changed:
        changed = False
        ks = sorted(list(cells_to_reprocess.keys()))
        for k in ks:
            for i, j in cells_to_reprocess[k]:
                candidate = get_min(result, i, j)
                if candidate < result[i][j]:
                    result[i][j] = candidate
                    changed = True

    return result