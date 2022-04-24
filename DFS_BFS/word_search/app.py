###########################################################################################
# leetcode problem https://leetcode.com/problems/word-search/
###########################################################################################

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(board, x: int, y: int, sequence: str) -> bool:
        q = [(x, y, 0, {(x, y)})]
        while len(q) > 0:
            pos_x, pos_y, i, seen = q.pop(-1)
            if i == len(sequence) - 1:
                return True
            candidates = [(pos_x, pos_y + 1), (pos_x, pos_y - 1), (pos_x + 1, pos_y), (pos_x - 1, pos_y)]
            for cx, cy in candidates:
                if 0 <= cx < len(board) \
                        and 0 <= cy < len(board[0]) \
                        and board[cx][cy] == sequence[i + 1] \
                        and (cx, cy) not in seen:
                    s = seen.copy()
                    s.add((cx, cy))
                    q.append((cx, cy, i + 1, s))

        return False

    if len(board) == 0 or len(word) == 0:  # corner case
        return False

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == word[0] and dfs(board, x, y, word):
                return True

    return False