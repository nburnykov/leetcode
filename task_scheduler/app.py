# https://leetcode.com/problems/task-scheduler/

from collections import deque, Counter
from heapq import heappush, heappop
from typing import List, Optional, Dict


def leastInterval(tasks: List[str], n: int) -> int:
    h = []
    result = []
    task_dict = {}
    for t in tasks:
        task_dict[t] = task_dict.get(t, 0) + 1
    for t, c in task_dict.items():
        heappush(h, (-1 * c, t))   # most frequent tasks go first
    tick = 0
    while len(h) > 0:
        next_tasks = []
        i = 0
        while i <= n:  # fill available window
            tick += 1
            if len(h) > 0:
                priority, task = heappop(h)
                result.append(task)
                if priority != -1:  # needs to be repeated next time
                    next_tasks.append((priority + 1, task))
            else:
                result.append(None)

            if len(h) == 0 and len(next_tasks) == 0:
                break
            else:
                i += 1

        for nt in next_tasks:
            heappush(h, nt)
    return tick













def leastIntervalLC(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    result = []
    curr_time, h = 0, []
    for k, v in Counter(tasks).items():
        heappush(h, (-1 * v, k))
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x, y = heappop(h)
                result.append(y)
                if x != -1:
                    temp.append((x + 1, y))
            else:
                result.append(None)
            if not h and not temp:
                break
            else:
                i += 1
        for item in temp:
            heappush(h, item)
    return curr_time




