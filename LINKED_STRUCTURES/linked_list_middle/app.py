###########################################################################################
# leetcode problem https://leetcode.com/problems/middle-of-the-linked-list/
###########################################################################################
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return

    current = head
    counter = 0
    middle_index = 0
    while current is not None:
        quotient = counter // 2
        middle = counter / 2
        if quotient == middle:
            middle_index = middle
        else:
            middle_index = quotient + 1
        counter += 1
        current = current.next

    current = head
    counter = 0
    while counter < middle_index:  # set current pointer to the middle of the linked list
        counter += 1
        current = current.next

    return current
