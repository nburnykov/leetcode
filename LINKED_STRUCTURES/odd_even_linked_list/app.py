from typing import Optional

from utils import ListNode


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    odd = ListNode()
    even = ListNode()
    even_head = even
    odd.next = head

    leader = head
    follower = odd
    count = 1
    while leader:
        if count % 2 == 0:
            even.next = leader
            even = even.next
            leader = leader.next
            follower.next = leader
        else:
            leader = leader.next
            follower = follower.next
        count += 1

    even.next = None
    follower.next = even_head.next

    return head





