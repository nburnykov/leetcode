###########################################################################################
# leetcode problem https://leetcode.com/problems/remove-nth-node-from-end-of-list/
###########################################################################################
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd_old(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return

    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next

    remove_index = length - n

    index_a = remove_index - 1
    index_b = remove_index + 1
    end_a = None
    end_b = None

    current = head
    counter = 0
    while counter < length:
        if counter == index_a:
            end_a = current
        if counter == index_b:
            end_b = current
            break
        counter += 1
        current = current.next

    if end_a is not None:
        end_a.next = end_b
        return head

    if end_a is None and end_b is not None:
        return end_b

    return


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return None

    dummy = ListNode()
    dummy.next = head
    current = dummy
    ln = 0
    while current.next is not None:  # find list length
        ln += 1
        current = current.next

    index_to_remove = ln - n

    leader = head
    follower = dummy
    for i in range(index_to_remove):
        leader = leader.next
        follower = follower.next

    follower.next = leader.next  # remove leader

    return dummy.next