from LINKED_STRUCTURES.swap_nodes_in_pairs.app import swapPairs
from utils import create_linked_list, read_linked_list


def test_case_1():
    head = [1, 2, 3, 4]
    result = [2, 1, 4, 3]
    llh = create_linked_list(head)
    assert read_linked_list(swapPairs(llh)) == result


def test_case_2():
    head = [1, 2, 3, 4, 5]
    result = [2, 1, 4, 3, 5]
    llh = create_linked_list(head)
    assert read_linked_list(swapPairs(llh)) == result

def test_case_3():
    head = [1]
    result = [1]
    llh = create_linked_list(head)
    assert read_linked_list(swapPairs(llh)) == result

def test_case_4():
    head = []
    result = []
    llh = create_linked_list(head)
    assert read_linked_list(swapPairs(llh)) == result