from typing import List, Optional

from remove_nth_node.remove_nth_node import ListNode, removeNthFromEnd


def create_linked_list(nums: List[int]) -> ListNode:
    result = None

    for n in nums[::-1]:
        r = ListNode()
        r.val = n
        r.next = result
        result = r

    return result


def read_linked_list(l: Optional[ListNode]) -> list:
    if l is None:
        return []
    result = [l.val]
    l_p = l.next
    while l_p is not None:
        result.append(l_p.val)
        l_p = l_p.next
    return result


def test_case_1():
    input = [1, 2, 3, 4, 5]
    n = 2
    output = [1, 2, 3, 5]
    ll = create_linked_list(input)
    assert read_linked_list(removeNthFromEnd(ll, n)) == output


def test_case_2():
    input = [1]
    n = 1
    output = []
    ll = create_linked_list(input)
    assert read_linked_list(removeNthFromEnd(ll, n)) == output

def test_case_3():
    input = [1, 2]
    n = 1
    output = [1]
    ll = create_linked_list(input)
    assert read_linked_list(removeNthFromEnd(ll, n)) == output