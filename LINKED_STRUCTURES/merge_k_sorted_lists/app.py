###########################################################################################
# leetcode problem https://leetcode.com/problems/merge-k-sorted-lists/
###########################################################################################

from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []

    for ln in lists:  # heap init
        if ln:
            heappush(heap, (ln.val, id(ln), ln.next))

    node_current = None
    node_head = None

    while len(heap) > 0:
        v, _, n = heappop(heap)
        ln = ListNode(v)
        if not node_current:
            node_current = ln
            node_head = ln
        else:
            node_current.next = ln
            node_current = ln
        if n:
            heappush(heap, (n.val, id(n), n.next))

    return node_head

