###########################################################################################
# leetcode problem  https://leetcode.com/problems/merge-intervals/
###########################################################################################

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    to_merge = intervals[0]
    result = []
    for start, end in intervals[1:]:
        tm_start, tm_end = to_merge
        if max(tm_start, start) <= min(tm_end, end):  # intervals can be merged
            to_merge = [min(tm_start, start), max(tm_end, end)]  # expand interval
        else:
            result.append(to_merge)  # replace to_merge with current
            to_merge = [start, end]

    result.append(to_merge)
    return result
