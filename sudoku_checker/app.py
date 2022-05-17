from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # check rows
    for row in range(9):
        seen = set()
        for col in range(9):
            val = board[row][col]
            if val in seen:
                return False
            if val != '.':
                seen.add(val)

    # check columns
    for col in range(9):
        seen = set()
        for row in range(9):
            val = board[row][col]
            if val in seen:
                return False
            if val != '.':
                seen.add(val)

    # check squares
    for x in range(3):
        for y in range(3):
            seen = set()
            for x_a in range(x * 3, x * 3 + 3):
                for y_a in range(y * 3, y * 3 + 3):
                    val = board[x_a][y_a]
                    if val in seen:
                        return False
                    if val != '.':
                        seen.add(val)

    return True
