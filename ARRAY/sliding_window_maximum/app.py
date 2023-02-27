# https://leetcode.com/problems/sliding-window-maximum

from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    Monotonic queue concept
    """
    q = deque([])
    result = []
    for index_first in range(0, len(nums)):
        index_second = index_first - k

        # queue: 8 6 4 1, el to insert: 7 -> queue: 8 7
        while len(q) > 0 and nums[q[-1]] <= nums[index_first]:
            q.pop()
        q.append(index_first)

        if len(q) > 0 and q[0] == index_second:
            q.popleft()
        if index_second >= -1:
            result.append(nums[q[0]])

    return result
