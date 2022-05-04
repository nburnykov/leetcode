###########################################################################################
# leetcode problem https://leetcode.com/problems/merge-two-sorted-lists/submissions/
###########################################################################################

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if (list1 and list2) is None:
        return list1 or list2

    result_head = None
    result_last = None
    while True:
        if (list1 and list2) is not None:
            if list1.val < list2.val:
                if result_last:
                    result_last.next = list1
                else:
                    result_head = list1
                result_last = list1
                list1 = list1.next
            else:
                if result_last:
                    result_last.next = list2
                else:
                    result_head = list2
                result_last = list2
                list2 = list2.next
        else:
            result_last.next = list1 or list2
            return result_head