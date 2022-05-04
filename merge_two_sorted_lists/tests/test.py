from merge_two_sorted_lists.app import mergeTwoLists
from utils import create_linked_list, read_linked_list


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