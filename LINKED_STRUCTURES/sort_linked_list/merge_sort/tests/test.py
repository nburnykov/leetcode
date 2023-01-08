from LINKED_STRUCTURES.sort_linked_list.merge_sort.app import merge_sort_recursive, merge_sort_iterative


def test_case_1():
    data = [12, 3, 5, 1, 2, 0, 6, 8]
    result = [0, 1, 2, 3, 5, 6, 8, 12]

    assert merge_sort_recursive(data) == result


def test_case_2():
    data = [12, 3, 5, 1, 2, 0, 6]
    result = [0, 1, 2, 3, 5, 6, 12]

    assert merge_sort_recursive(data) == result


def test_case_3():
    data = [12, 3, 5, 1, 2, 0, 6, 8]
    result = [0, 1, 2, 3, 5, 6, 8, 12]

    merge_sort_iterative(data)
    assert data == result


def test_case_4():
    data = [12, 3, 5, 1, 2, 0, 6]
    result = [0, 1, 2, 3, 5, 6, 12]

    merge_sort_iterative(data)
    assert data == result