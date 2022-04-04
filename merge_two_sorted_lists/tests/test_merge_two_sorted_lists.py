from typing import List

from merge_two_sorted_lists.merge_two_sorted_lists import ListNode, mergeTwoLists


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
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    output = [1, 1, 2, 3, 4, 4]
    ll1 = create_linked_list(list1)
    ll2 = create_linked_list(list2)
    assert read_linked_list(mergeTwoLists(ll1, ll2)) == output


def test_case_2():
    list1 = []
    list2 = []
    output = []
    ll1 = create_linked_list(list1)
    ll2 = create_linked_list(list2)
    assert read_linked_list(mergeTwoLists(ll1, ll2)) == output


def test_case_3():
    list1 = []
    list2 = [0]
    output = [0]
    ll1 = create_linked_list(list1)
    ll2 = create_linked_list(list2)
    assert read_linked_list(mergeTwoLists(ll1, ll2)) == output