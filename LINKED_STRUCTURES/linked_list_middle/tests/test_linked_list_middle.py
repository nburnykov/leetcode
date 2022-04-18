from typing import List

from LINKED_STRUCTURES.linked_list_middle.linked_list_middle import ListNode, middleNode


def create_linked_list(nums: List[int]) -> ListNode:
    result = None

    for n in nums[::-1]:
        r = ListNode()
        r.val = n
        r.next = result
        result = r

    return result


def read_linked_list(l: ListNode) -> list:
    result = [l.val]
    l_p = l.next
    while l_p is not None:
        result.append(l_p.val)
        l_p = l_p.next
    return result


def test_case_1():
    input = [1, 2, 3, 4, 5]
    output = [3, 4, 5]
    ll = create_linked_list(input)
    assert read_linked_list(middleNode(ll)) == output

def test_case_2():
    input = [1, 2, 3, 4, 5, 6]
    output = [4, 5, 6]
    ll = create_linked_list(input)
    assert read_linked_list(middleNode(ll)) == output

def test_case_3():
    input = [1]
    output = [1]
    ll = create_linked_list(input)
    assert read_linked_list(middleNode(ll)) == output