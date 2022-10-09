from LINKED_STRUCTURES.palindrome_ll.app import isPalindrome
from utils import create_linked_list


def test_case_1():
    a = [1, 2, 3, 4, 5]
    ll = create_linked_list(a)
    assert not isPalindrome(ll)

def test_case_2():
    a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    ll = create_linked_list(a)
    assert isPalindrome(ll)


def test_case_3():
    a = [1, 2, 2, 1]
    ll = create_linked_list(a)
    assert isPalindrome(ll)
