###########################################################################################
# leetcode problem https://leetcode.com/problems/reverse-linked-list/
###########################################################################################

# Definition for singly-linked list.
from typing import Optional

from utils import ListNode


def reverseList1(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    current = head
    result = ListNode(current.val, None)
    while current.next:
        current = current.next
        ln = ListNode(current.val, result)
        result = ln
    return result

def reverseList(head: Optional[ListNode], prev=None) -> Optional[ListNode]:
    if not head:
        return prev
    n = head.next
    head.next = prev
    return reverseList(n, head)