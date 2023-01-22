# https://leetcode.com/problems/perfect-squares
from collections import deque


def numSquares(n: int) -> int:
    q = deque([(0, n)])
    visited = set()
    while len(q) > 0:
        count, n = q.popleft()
        if n == 0:
            return count
        if n < 0:
            continue
        k = 1
        while k * k <= n:
            next_value = n - k * k
            if next_value not in visited:
                q.append((count + 1, next_value))
                visited.add(next_value)
            k += 1
