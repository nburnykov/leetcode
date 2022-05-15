###########################################################################################
# leetcode problem https://leetcode.com/problems/network-delay-time/
###########################################################################################

from collections import deque, defaultdict
from heapq import heappop, heappush
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    node_time = {k: 0}  # start node has zero time to reach
    q = deque([(k, 0)])

    graph = dict()
    for node_a, node_b, t in times:
        graph.setdefault(node_a, []).append((node_b, t))

    while len(q) > 0:  # BFS
        node, time = q.popleft()
        for node_b, t in graph.get(node, []):
            node_b_time = time + t
            if node_b_time < node_time.get(node_b, float('inf')):  # time has been improved
                node_time[node_b] = node_b_time
                q.append((node_b, time + t))

    max_time = 0
    for node in range(1, n+1):
        max_time = max(max_time, node_time.get(node, float('inf')))

    return max_time if max_time != float('inf') else -1


def networkDelayTimeHeap(times: List[List[int]], n: int, k: int) -> int:
    q = [(0, k)]
    times_min = dict()
    graph = dict()
    for node_a, node_b, t in times:
        graph.setdefault(node_a, []).append((node_b, t))
    while q:
        time, node = heappop(q)
        if node not in times_min:
            times_min[node] = time
            if len(times_min) == n:  # early stopping
                return max(times_min.values())
            for node_b, t in graph.get(node, []):
                heappush(q, (time + t, node_b))
    return  -1

