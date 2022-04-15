from add_two_numbers.app import addTwoNumbers
from utils import create_linked_list, read_linked_list


def test_case_ll():
    ll = create_linked_list([1, 2, 3])
    assert read_linked_list(ll) == [1, 2, 3]


def test_case_1():
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    ll = addTwoNumbers(l1, l2)
    assert read_linked_list(ll) == [7, 0, 8]


def test_case_2():
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    ll = addTwoNumbers(l1, l2)
    assert read_linked_list(ll) == [0]


def test_case_3():
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    ll = addTwoNumbers(l1, l2)
    assert read_linked_list(ll) == [8, 9, 9, 9, 0, 0, 0, 1]
