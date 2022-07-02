###########################################################################################
# leetcode problem  https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
###########################################################################################
from typing import List


def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    hc = [0] + sorted(horizontalCuts) + [h]
    vc = [0] + sorted(verticalCuts) + [w]

    max_h = 1
    for i in range(1, len(hc)):
        max_h = max(max_h, hc[i] - hc[i - 1])

    max_v = 1
    for i in range(1, len(vc)):
        max_v = max(max_v, vc[i] - vc[i - 1])

    return (max_h * max_v) % (1e9 + 7)

