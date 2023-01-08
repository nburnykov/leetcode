from ARRAY.remove_duplicates_sorted.app import removeDuplicates


def test_case_1():
    nums = [1, 1, 2]
    removeDuplicates(nums)

    assert nums == [1, 2]


def test_case_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeDuplicates(nums)

    assert nums == [0, 1, 2, 3, 4]
