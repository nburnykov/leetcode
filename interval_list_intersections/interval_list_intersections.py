###########################################################################################
# leetcode problem https://leetcode.com/problems/interval-list-intersections/
###########################################################################################

from typing import List


def intervalIntersection2(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    if min(len(firstList), len(secondList)) == 0:  # corner case
        return []

    curr, opp = firstList, secondList
    i_c, i_o = 0, 0

    open_time, close_time = None, None

    result = []
    while i_o < len(opp) and i_c < len(curr):
        if open_time is None:  # no intersection registered
            if curr[i_c][0] > opp[i_o][0]:  # places the closest interval first (as current)
                curr, opp = opp, curr
                i_c, i_o = i_o, i_c

            if curr[i_c][0] <= opp[i_o][0] <= curr[i_c][1]:  # opposite interval starts within the current
                open_time = opp[i_o][0]
            else:
                i_c += 1  # moves current further
                continue
        else:   # intersection start has been found
            if curr[i_c][0] <= opp[i_o][1] <= curr[i_c][1]:  # opposite interval ends within the current
                close_time = opp[i_o][1]
                i_o += 1  # moves opposite further
            else:
                curr, opp = opp, curr  # the opposite ends after the current (switch current <-> opposite)
                i_c, i_o = i_o, i_c

        if open_time is not None and close_time is not None:  # registers intersection
            result.append([open_time, close_time])
            open_time, close_time = None, None  # resets the intersection

    return result


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i1, i2 = 0, 0
    result = []

    while i1 < len(firstList) and i2 < len(secondList):
        l1 = firstList[i1]
        l2 = secondList[i2]

        max_start = max(l1[0], l2[0])
        min_end = min(l1[1], l2[1])
        if max_start <= min_end:
            result.append([max_start, min_end])

        if l1[1] < l2[1]:
            i1 += 1
        else:
            i2 += 1

    return result
