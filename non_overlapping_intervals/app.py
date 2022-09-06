###########################################################################################
# leetcode problem  https://leetcode.com/problems/non-overlapping-intervals/
###########################################################################################
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    in case of overlap delete interval with longest end
    |----------------------| <- delete this
         |-------| |-----|
    """
    intervals.sort(key=lambda x: x[0])
    curr = intervals[0]
    cnt = 0
    for inter in intervals[1:]:
        if max(curr[0], inter[0]) < min(curr[1], inter[1]):
            cnt += 1
            if inter[1] > curr[1]:  # delete inter
                continue
        curr = inter
    return cnt
