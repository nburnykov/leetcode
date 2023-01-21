# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    def dfs(start_point: (int, int)) -> set:
        stack = [start_point]
        seen = {start_point}
        while len(stack) > 0:
            i, j = stack.pop(-1)
            candidates = {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)} - seen
            for ci, cj in candidates:
                if 0 <= ci < len(heights) and 0 <= cj < len(heights[0]) and heights[ci][cj] >= heights[i][j]:
                    stack.append((ci, cj))
                    seen.add((ci, cj))
        return seen

    seen_pacific = set()
    seen_atlantic = set()
    for j in range(len(heights[0])):
        seen_pacific.update(dfs((0, j)))
        seen_atlantic.update(dfs((len(heights)- 1, j)))
    for i in range(len(heights)):
        seen_pacific.update(dfs((i, 0)))
        seen_atlantic.update(dfs((i, len(heights[0])- 1)))

    return sorted(map(list, seen_pacific & seen_atlantic))



