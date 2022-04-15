###########################################################################################
# leetcode problem
###########################################################################################

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None and l2 is None:  # edge case 1
        return

    if l1 is None and l2 is not None:  # edge case 2
        return l2

    if l1 is not None and l2 is None:  # edge case 3
        return l1

    l1_p = l1
    l2_p = l2
    val_1 = l1_p.val
    val_2 = l2_p.val
    val_add = 0

    current = None
    first_element = None

    while True:
        val_sum = val_1 + val_2 + val_add
        val_curr = val_sum % 10
        val_add = val_sum // 10

        r = ListNode()
        r.val = val_curr
        r.next = None

        if current is not None:
            current.next = r
        else:
            first_element = r

        current = r

        l1_p = l1_p.next if l1_p is not None else None
        l2_p = l2_p.next if l2_p is not None else None

        if l1_p is not None:
            val_1 = l1_p.val
        else:
            val_1 = 0

        if l2_p is not None:
            val_2 = l2_p.val
        else:
            val_2 = 0

        if l1_p is None and l2_p is None and val_add == 0:
            return first_element


