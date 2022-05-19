###########################################################################################
# leetcode problem https://leetcode.com/problems/critical-connections-in-a-network/
###########################################################################################
from typing import List


def criticalConnections2(n: int, connections: List[List[int]]) -> List[List[int]]:
    lows = [None] * n
    ids = [None] * n
    visited = [False] * n

    lows[0] = 0

    graph = dict()
    for a, b in connections:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    q = [(0, -1)]
    order = 0
    is_forward = True
    parent_id = None
    while len(q) > 0:  # DFS
        node, parent = q[-1]
        if not is_forward:
            is_forward = True
            lows[node] = min(lows[node], lows[parent_id])

        for node_b in graph.get(node, {}):
            if node_b == parent:
                continue
            if not visited[node_b]:
                visited[node_b] = True
                order += 1
                lows[node_b] = order
                ids[node_b] = order
                q.append((node_b, node))
                break
            else:
                lows[node] = min(ids[node_b], lows[node])

        if q[-1] == (node, parent):  # queue hasn't appended, time to backtrack
            q.pop(-1)
            is_forward = False
            parent_id = node

    result = [[node_a, node_b] for node_a, node_b in connections if lows[node_a] != lows[node_b]]

    return result


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    def dfs(current, parent, order):
        order += 1
        lows[current] = ids[current] = order

        for b in graph.get(current, {}):
            if b == parent:
                continue
            if ids[b] is None:
                dfs(b, current, order)
                lows[current] = min(lows[current], lows[b])
                if ids[current] < lows[b]:
                    result.append([current, b])
            else:
                lows[current] = min(lows[current], ids[b])

    lows = [None] * n
    ids = [None] * n

    lows[0] = 0

    graph = dict()
    for a, b in connections:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    result = []

    dfs(0, -1, 0)

    return result
