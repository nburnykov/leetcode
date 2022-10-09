###########################################################################################
# leetcode problem  https://leetcode.com/problems/palindrome-linked-list/
###########################################################################################
from typing import Optional
from utils import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    node = head
    ll2 = None
    ll2_nxt = None
    while node:
        ll2 = node
        ll2.next = ll2_nxt
        ll2_nxt = ll2
        node = node.next

    return ll2


