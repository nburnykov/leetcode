###########################################################################################
# leetcode problem  https://leetcode.com/problems/linked-list-cycle-ii/
###########################################################################################
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
