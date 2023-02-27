###########################################################################################
# leetcode problem  https://leetcode.com/problems/partition-labels/
###########################################################################################
from collections import OrderedDict
from typing import List


def partitionLabels(s: str) -> List[int]:
    """
    The same idea as in merge intervals problem
    """
    labelmap = OrderedDict()
    for pos, char in enumerate(s):
        if char not in labelmap:
            labelmap[char] = [pos, pos]
        else:
            start, _ = labelmap[char]
            labelmap[char] = start, pos

    result = []
    diap = None, None
    for start, end in labelmap.values():
        if diap == (None, None):
            diap = start, end
            continue

        if max(start, diap[0]) <= min(end, diap[1]):
            ds, de = diap
            diap = ds, max(end, de)
        else:
            result.append(diap[1] - diap[0] + 1)
            diap = start, end

    result.append(diap[1] - diap[0] + 1)

    return result

