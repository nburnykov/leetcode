from LINKED_STRUCTURES.reverse_linked_list.app import reverseList
from utils import create_linked_list, read_linked_list


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