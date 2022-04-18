###########################################################################################
# leetcode problem https://leetcode.com/problems/surrounded-regions/
###########################################################################################

from collections import deque
from typing import List, Tuple


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def dfs(board: List[List[str]], target: Tuple[int, int]):
        q = deque([target])
        while len(q) > 0:
            x, y = q.popleft()
            board[x][y] = 'B'
            candidates = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
            for cx, cy in candidates:
                if 0 <= cx < len(board) and 0 <= cy < len(board[0]) and board[cx][cy] == 'O':
                    board[cx][cy] = 'B'
                    q.append((cx, cy))

    for i in [0, len(board) - 1]:
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                dfs(board, (i, j))

    for j in [0, len(board[0]) - 1]:
        for i in range(len(board)):
            if board[i][j] == 'O':
                dfs(board, (i, j))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'B':
                board[i][j] = 'O'
