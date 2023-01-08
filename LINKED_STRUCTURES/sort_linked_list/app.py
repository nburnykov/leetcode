###########################################################################################
# leetcode problem  https://leetcode.com/problems/sort-list/
###########################################################################################

from typing import Optional

from utils import ListNode


def get_sublist(head: Optional[ListNode], length: int) -> (Optional[ListNode], Optional[ListNode]):
    dummy = ListNode()
    dummy.next = head
    cursor = dummy
    i = 0
    while cursor.next and i < length:
        cursor = cursor.next
        i += 1

    next_sublist = cursor.next
    cursor.next = None

    return dummy.next, next_sublist


def merge_lists(list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode()
    cursor = dummy_head
    while list_1 and list_2:
        if list_1.val < list_2.val:
            cursor.next = list_1
            cursor = cursor.next
            list_1 = list_1.next
        else:
            cursor.next = list_2
            cursor = cursor.next
            list_2 = list_2.next
    cursor.next = list_1 or list_2
    return dummy_head.next


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    pointer_start = ListNode()
    pointer_start.next = head

    cursor = head
    ln = 0
    while cursor:
        cursor = cursor.next
        ln += 1

    step, step_max = 2, 2
    while step_max < ln:  # find maximum step that covers entire list
        step_max *= 2

    dummy_head = pointer_start

    while step <= step_max:

        pointer_start = dummy_head
        pointer_end = pointer_start

        while pointer_end:
            step_half = step // 2
            right, pointer_end = get_sublist(pointer_start.next, step_half)
            left, pointer_end = get_sublist(pointer_end, step_half)

            ll_merged = merge_lists(right, left)
            if ll_merged:
                cursor = ll_merged
                while cursor.next:
                    cursor = cursor.next

                pointer_start.next = ll_merged
                cursor.next = pointer_end

                pointer_start = cursor

        step *= 2

    return dummy_head.next










