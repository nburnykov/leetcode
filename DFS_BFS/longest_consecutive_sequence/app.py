###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-consecutive-sequence/
###########################################################################################

from collections import deque
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    seq = set(nums)

    max_c = 0
    while len(seq) > 0:
        n = seq.pop()
        c = 1
        q = deque([(n + 1, 'f'), (n - 1, 'b')])
        while len(q) > 0:  # BFS
            current, direction = q.popleft()
            if current in seq:
                seq.remove(current)
                c += 1
                if direction == 'f':
                    q.append((current + 1, 'f'))
                else:
                    q.append((current - 1, 'b'))
        max_c = max(max_c, c)

    return max_c


