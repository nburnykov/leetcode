###########################################################################################
# leetcode problem https://leetcode.com/problems/01-matrix/
###########################################################################################

from typing import List, Optional
from collections import deque


def updateMatrix2(mat: List[List[int]]) -> List[List[int]]:  # BFS based solution
    if not mat:
        return []

    visited_nodes = set()
    q = deque()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                visited_nodes.add((i, j))
                q.append((i, j))

    while len(q) > 0:
        i, j = q.popleft()
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and (x, y) not in visited_nodes:
                mat[x][y] = mat[i][j] + 1
                q.append((x, y))
                visited_nodes.add((x, y))

    return mat


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    if not mat:
        return []

    result = [[float("inf")] * len(mat[0]) for _ in mat]

    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if mat[i][j] == 0:
                result[i][j] = 0
            else:
                cand_a = result[i][j - 1] + 1 if j > 0 else float("inf")
                cand_b = result[i - 1][j] + 1 if i > 0 else float("inf")
                candidate = min(cand_a, cand_b)
                if result[i][j] > candidate:
                    result[i][j] = candidate

    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat[0]) - 1, -1, -1):
            cand_a = result[i][j + 1] + 1 if j < len(mat[0]) - 1 else float("inf")
            cand_b = result[i + 1][j] + 1 if i < len(mat) - 1 else float("inf")
            candidate = min(cand_a, cand_b)
            if result[i][j] > candidate:
                result[i][j] = candidate

    return result
