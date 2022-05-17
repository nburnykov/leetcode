from LINKED_STRUCTURES.reverse_k_group.app import reverseKGroup
from utils import create_linked_list, read_linked_list


def test_case_1():
    head = [1, 2, 3, 4, 5]
    k = 2
    r = [2, 1, 4, 3, 5]
    llhead = create_linked_list(head)
    assert read_linked_list(reverseKGroup(llhead, k)) == r


def test_case_2():
    head = [1, 2, 3, 4, 5]
    k = 3
    r = [3, 2, 1, 4, 5]
    llhead = create_linked_list(head)
    assert read_linked_list(reverseKGroup(llhead, k)) == r
