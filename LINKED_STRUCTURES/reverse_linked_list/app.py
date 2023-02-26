###########################################################################################
# leetcode problem https://leetcode.com/problems/reverse-linked-list/
###########################################################################################

# Definition for singly-linked list.
from typing import Optional

from utils import ListNode

def reverseList1(head: Optional[ListNode], prev=None) -> Optional[ListNode]:
    if not head:
        return prev
    n = head.next
    head.next = prev
    return reverseList(n, head)


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current_node, prev_node = head, None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node