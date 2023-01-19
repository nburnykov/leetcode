from LINKED_STRUCTURES.sorted_array_to_bst.app import sortedArrayToBST


def test_case_1():
    nums = [-10, -3, 0, 5, 9]
    bst = sortedArrayToBST(nums)
    print(bst)