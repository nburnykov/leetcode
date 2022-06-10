from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []

    for i, (start, end) in enumerate(intervals):
        if max(start, newInterval[0]) <= min(end, newInterval[1]):  # if intersection found then expand new interval
            newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        else:
            if start > newInterval[1]:  # current interval is behind newInterval
                result += [newInterval] + intervals[i:]
                return result
            result.append([start, end])

    if newInterval:  # still not inserted
        return result + [newInterval]

