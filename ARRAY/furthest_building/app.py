###########################################################################################
# leetcode problem  https://leetcode.com/problems/furthest-building-you-can-reach/
###########################################################################################

from typing import List
from heapq import heappush, heappop


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    min_heights = []
    for i in range(1, len(heights)):
        height_diff = heights[i] - heights[i - 1]
        if height_diff < 0:  # if jump down
            continue
        heappush(min_heights, height_diff)
        if len(min_heights) > ladders:  # if ladders are over start to fill min gap with bricks
            bricks -= heappop(min_heights)
        if bricks < 0:  # bricks are over
            return i - 1
    return len(heights) - 1  # walk all the buildings

