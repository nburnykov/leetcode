###########################################################################################
# leetcode problem  https://leetcode.com/problems/my-calendar-i/
###########################################################################################
from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.interval_list = SortedDict([])

    def book(self, start: int, end: int) -> bool:
        pos = self.interval_list.bisect_left(start)
        lp, rp = pos - 1, pos

        # find the nearest left
        if lp >= 0:
            left_start = self.interval_list.keys()[lp]
            left_end = self.interval_list[left_start]
            if left_end > start:
                return False

        # find the nearest right
        if rp < len(self.interval_list):
            right_start = self.interval_list.keys()[rp]
            if right_start < end:
                return False

        self.interval_list[start] = end
        return True
