###########################################################################################
# leetcode problem  https://leetcode.com/problems/rotate-list/
###########################################################################################

from typing import Optional

from utils import ListNode


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:

    if head is None:
        return
    if k == 0:
        return head

    # determine end of the list
    node_end = head
    i_end = 0
    while node_end.next is not None:
        node_end = node_end.next
        i_end += 1

    # determine pivot node index
    node_pivot = head
    i_pivot = (i_end - k) % (i_end + 1)  # in case of k > len(linked_list)

    for _ in range(i_pivot):
        node_pivot = node_pivot.next

    head_dummy = ListNode()
    head_dummy.next = head

    # rotation
    node_end.next = head_dummy.next
    head_dummy.next = node_pivot.next
    node_pivot.next = None

    return head_dummy.next

