###########################################################################################
# leetcode problem  https://leetcode.com/problems/palindrome-linked-list/
###########################################################################################
from typing import Optional
from utils import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    # find middle node
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second half from slow pointer to the end
    ll2 = ll2_nxt = None
    while slow:
        ll2 = slow
        slow = slow.next
        ll2.next = ll2_nxt
        ll2_nxt = ll2

    # compare first untouched part and second reversed
    while ll2:
        if head.val != ll2.val:
            return False
        head = head.next
        ll2 = ll2.next

    return True



