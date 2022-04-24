###########################################################################################
# leetcode problem https://leetcode.com/problems/all-paths-from-source-to-target/
###########################################################################################

from collections import deque
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    if len(graph) == 0:
        return []
    q = deque([(i, [0]) for i in graph[0]])

    result = []
    while len(q) > 0:
        next_item, path = q.popleft()
        path.append(next_item)
        if next_item == len(graph) - 1:
            result.append(path)
        for i in graph[next_item]:
            q.append((i, path.copy()))

    return result