from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return 0

    max_area = 0

    for i in range(len(grid)):  # search for a new island
        for j in range(len(grid[0])):
            if grid[i][j] == 1:

                island_squares = [(i, j)]
                candidate_area = 0
                grid[i][j] = 0

                while len(island_squares) > 0:
                    x, y = island_squares.pop(-1)
                    candidate_area += 1

                    candidate_coord = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    for x, y in candidate_coord:
                        if (0 <= x <= len(grid) - 1) \
                                and (0 <= y <= len(grid[0]) - 1) \
                                and grid[x][y]:  # square lies within grid
                            island_squares.append((x, y))
                            grid[x][y] = 0

                if candidate_area > max_area:
                    max_area = candidate_area

    return max_area