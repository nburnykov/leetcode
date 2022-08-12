###########################################################################################
# leetcode problem  https://leetcode.com/problems/max-points-on-a-line/
###########################################################################################

from math import gcd
from typing import List


def maxPoints(points: List[List[int]]) -> int:
    if len(points) < 3:
        return len(points)

    processed_points = []
    m = 0
    for x, y in points:
        ks = dict()
        for x_p, y_p in processed_points:

            if x == x_p:  # horizontal line has found
                k = ('v', x)
                ks[k] = ks.get(k, 1) + 1
                m = max(m, ks[k])

            if y == y_p:  # vertical line has found
                k = ('h', y)
                ks[k] = ks.get(k, 1) + 1
                m = max(m, ks[k])

            dy = y_p - y
            dx = x_p - x
            if dy < 0:
                dx, dy = -dx, -dy
            g = gcd(dx, dy)
            k = dx // g, dy // g

            ks[k] = ks.get(k, 1) + 1
            m = max(m, ks[k])

        processed_points.append((x, y))

    return m