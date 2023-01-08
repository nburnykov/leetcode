from LINKED_STRUCTURES.sort_linked_list.app import get_sublist, merge_lists, sortList
from utils import create_linked_list, read_linked_list


def test_get_sublist_1():
    data = [1, 2, 3, 4, 5]
    result_sublist = [1, 2, 3]
    length = 3
    result_end = [4, 5]

    ll_data = create_linked_list(data)
    sublist, sublist_end = get_sublist(ll_data, length)

    assert read_linked_list(sublist) == result_sublist
    assert read_linked_list(sublist_end) == result_end


def test_get_sublist_2():
    data = [1, 2, 3, 4, 5]
    result_sublist = [1, 2, 3, 4, 5]
    length = 8
    result_end = []

    ll_data = create_linked_list(data)
    sublist, sublist_end = get_sublist(ll_data, length)

    assert read_linked_list(sublist) == result_sublist
    assert read_linked_list(sublist_end) == result_end


def test_get_sublist_3():
    assert get_sublist(None, 10) == (None, None)


def test_merge_lists_1():
    l1 = [1, 5, 10, 15, 20]
    l2 = [2, 4, 6, 8]
    result = sorted(l1 + l2)

    ll_1 = create_linked_list(l1)
    ll_2 = create_linked_list(l2)

    merged_list = merge_lists(ll_1, ll_2)
    assert read_linked_list(merged_list) == result


def test_sort_linked_list_1():
    data = [18, 115, 28, 33, 44, 1, 6, 5]
    result = sorted(data)

    ll_data = create_linked_list(data)
    ll_sorted = sortList(ll_data)
    assert read_linked_list(ll_sorted) == result


def test_sort_linked_list_2():
    data = [18, 115, 28, 33, 44, 1, 6, 5, -5]
    result = sorted(data)

    ll_data = create_linked_list(data)
    ll_sorted = sortList(ll_data)
    assert read_linked_list(ll_sorted) == result
