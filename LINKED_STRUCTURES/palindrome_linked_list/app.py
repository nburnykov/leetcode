###########################################################################################
# leetcode problem  https://leetcode.com/problems/palindrome-linked-list/
###########################################################################################
from typing import Optional
from utils import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    current = None
    nxt = None
    while slow:
        current = slow
        slow = slow.next
        current.next = nxt
        nxt = current

    while current:
        if head.val != current.val:
            return False
        head = head.next
        current = current.next

    return True



