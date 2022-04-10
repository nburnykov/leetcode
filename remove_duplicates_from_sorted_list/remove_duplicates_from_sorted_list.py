# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from utils import ListNode


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    def next_node(current: ListNode) -> Optional[ListNode]:
        in_chain = False  # in chain of the same valued nodes
        while True:
            if current.next is None:
                return current if not in_chain else None
            if current.val != current.next.val:
                if in_chain:  # switch to the next candidate
                    current = current.next
                    in_chain = False
                else:
                    return current  # proven single node
            else:
                in_chain = True
                current = current.next

    # corner cases
    if not head:
        return
    if not head.next:  # contains only single element
        return head

    tn = ListNode()  # a helper node to maintain invariant
    tn.next = head
    c = tn
    while c.next:
        c.next = next_node(c.next)
        if c.next:
            c = c.next

    return tn.next
