from LINKED_STRUCTURES.rotate_list.app import rotateRight
from utils import create_linked_list, read_linked_list


def test_case_1():
    l = [1, 2, 3, 4, 5]
    k = 2
    r = [4, 5, 1, 2, 3]

    ll = create_linked_list(l)
    rll = rotateRight(ll, k)
    assert read_linked_list(rll) == r


def test_case_2():
    l = [0, 1, 2]
    k = 4
    r = [2, 0 ,1]

    ll = create_linked_list(l)
    rll = rotateRight(ll, k)
    assert read_linked_list(rll) == r


def test_case_3():
    l = [0, 1, 2]
    k = 0
    r = [0, 1, 2]

    ll = create_linked_list(l)
    rll = rotateRight(ll, k)
    assert read_linked_list(rll) == r


def test_case_4():
    l = [0, 1]
    k = 1
    r = [1, 0]

    ll = create_linked_list(l)
    rll = rotateRight(ll, k)
    assert read_linked_list(rll) == r

def test_case_5():
    l = [1, 2, 3, 4, 5]
    k = 1
    r = [5, 1, 2, 3, 4]


    ll = create_linked_list(l)
    rll = rotateRight(ll, k)
    assert read_linked_list(rll) == r