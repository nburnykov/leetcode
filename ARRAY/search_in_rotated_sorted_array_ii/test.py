from ARRAY.search_in_rotated_sorted_array_ii.app import search


def test_1():
    arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    assert search(arr, target)