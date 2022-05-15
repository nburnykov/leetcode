###########################################################################################
# leetcode problem https://leetcode.com/problems/swap-nodes-in-pairs/
###########################################################################################

from typing import Optional

from utils import ListNode


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    one = ListNode()
    one.next = head
    head = one
    while one.next and one.next.next:
        two = one.next
        three = one.next.next
        four = one.next.next.next

        two.next = four
        three.next = two
        one.next = three

        one = one.next.next  # move forward

    return head.next