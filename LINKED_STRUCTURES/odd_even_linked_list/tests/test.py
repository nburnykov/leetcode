from LINKED_STRUCTURES.odd_even_linked_list.app import oddEvenList
from utils import create_linked_list, read_linked_list


def test_case_1():
    head = [1, 2, 3, 4, 5]
    result = [1, 3, 5, 2, 4]

    assert read_linked_list(oddEvenList(create_linked_list(head))) == result


def test_case_2():
    head = [2, 1, 3, 5, 6, 4, 7]
    result = [2, 3, 6, 7, 1, 5, 4]

    assert read_linked_list(oddEvenList(create_linked_list(head))) == result


def test_case_3():

    assert oddEvenList(None) == None
