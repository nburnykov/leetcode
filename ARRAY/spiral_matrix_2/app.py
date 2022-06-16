from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    mtx = [[None] * n for _ in range(n)]

    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction_index = 0
    x, y = 0, 0
    val = 1
    mtx[x][y] = val
    change_count = 0
    while change_count < 2:
        x_new, y_new = x + direction[direction_index][0], y + direction[direction_index][1]
        if 0 <= x_new < n and 0 <= y_new < n and mtx[x_new][y_new] is None:
            x, y = x_new, y_new
            val += 1
            mtx[x][y] = val
            change_count = 0
        else:
            direction_index = (direction_index + 1) % 4
            change_count += 1

    return mtx

