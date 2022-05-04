from remove_duplicates_from_sorted_list.app import deleteDuplicates
from utils import create_linked_list, read_linked_list


def test_case_1():
    input = [1, 2, 3, 3, 4, 4, 5]
    output = [1, 2, 5]
    ll = create_linked_list(input)
    assert read_linked_list(deleteDuplicates(ll)) == output


def test_case_2():
    input = [1, 1, 1, 2, 3]
    output = [2, 3]
    ll = create_linked_list(input)
    assert read_linked_list(deleteDuplicates(ll)) == output


def test_case_3():
    input = [1, 1, 1]
    output = []
    ll = create_linked_list(input)
    assert read_linked_list(deleteDuplicates(ll)) == output


def test_case_4():
    input = [1, 1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 6, 6]
    output = [2, 3]
    ll = create_linked_list(input)
    assert read_linked_list(deleteDuplicates(ll)) == output
