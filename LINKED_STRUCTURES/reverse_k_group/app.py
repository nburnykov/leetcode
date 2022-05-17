###########################################################################################
# leetcode problem https://leetcode.com/problems/reverse-nodes-in-k-group/
###########################################################################################

from typing import Optional

from utils import ListNode


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    l1 = ListNode()
    l2 = head
    l1.next = l2
    head = l1

    while True:
        i = 0
        l_check = l2
        while l_check and i < k:  # check if there is a complete group ahead
            i += 1
            l_check = l_check.next

        if i < k:  # group incomplete - stop
            break

        for _ in range(k - 1):  # swap the nodes in complete group
            swap_node = l2.next
            l2.next = swap_node.next
            swap_node.next = l1.next
            l1.next = swap_node

        l1 = l2
        l2 = l1.next

    return head.next
