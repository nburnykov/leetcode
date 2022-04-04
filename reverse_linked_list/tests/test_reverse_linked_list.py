from typing import List

from reverse_linked_list.reverse_linked_list import ListNode, reverseList


def create_linked_list(nums: List[int]) -> ListNode:
    result = None

    for n in nums[::-1]:
        r = ListNode()
        r.val = n
        r.next = result
        result = r

    return result


def read_linked_list(l: ListNode) -> list:
    if not l:
        return []
    result = [l.val]
    l_p = l.next
    while l_p is not None:
        result.append(l_p.val)
        l_p = l_p.next
    return result


def test_case_1():
    l = [1, 2, 3, 4, 5]
    output = [5, 4, 3, 2, 1]
    ll = create_linked_list(l)
    assert read_linked_list(reverseList(ll)) == output

def test_case_2():
    l = [1, 2]
    output = [2, 1]
    ll = create_linked_list(l)
    assert read_linked_list(reverseList(ll)) == output