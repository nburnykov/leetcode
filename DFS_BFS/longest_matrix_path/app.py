###########################################################################################
# leetcode problem https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
###########################################################################################
from collections import deque
from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    DIR = [0, 1, 0, -1, 0]
    m, n = len(matrix), len(matrix[0])

    outDegree = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] <= matrix[r][c]: continue
                outDegree[r][c] += 1

    q = deque([])
    for r in range(m):
        for c in range(n):
            if outDegree[r][c] == 0:
                q.append([r, c])

    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] >= matrix[r][c]: continue
                outDegree[nr][nc] -= 1
                if outDegree[nr][nc] == 0:
                    q.append([nr, nc])

    return level


def longestIncreasingPathSlow(matrix: List[List[int]]) -> int:
    """
    toposort over DAG
    """

    h = len(matrix)
    w = len(matrix[0])
    if h == w == 1:  # edge case
        return 1

    # create a graph
    dag = dict()
    v = set()
    for x in range(h):
        for y in range(w):
            candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for cx, cy in candidates:
                if 0 <= cx < h and 0 <= cy < w and matrix[cx][cy] > matrix[x][y]:
                    a = w * x + y
                    b = w * cx + cy
                    dag.setdefault(a, []).append(b)  # fill with node ids
                    v.update({a, b})

    # toposort
    node_order = []  # result of toposort algo
    seen = set()
    while len(v) > 0:
        start = v.pop()
        q = [start]
        seen.add(start)
        while len(q) > 0:
            at = q[-1]
            stub = True
            for to in dag.get(at, []):
                if to in v:
                    v.remove(to)
                if to not in seen:
                    stub = False
                    q.append(to)
                    seen.add(to)
                    break
            if stub:
                node_order = [at] + node_order
                q.pop(-1)

    path_len = dict()
    for at in node_order:
        for to in dag.get(at, []):
            path_len[to] = max(path_len.get(to, 1), path_len.get(at, 1) + 1)


    return max(path_len.values())



