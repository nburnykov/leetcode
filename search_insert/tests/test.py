from search_insert.app import Solution


def test_case_1():
    nums = [1, 3, 5, 6]
    target = 5
    assert Solution().searchInsert(nums, target) == 2


def test_case_2():
    nums = [1, 3, 5, 6]
    target = 2
    assert Solution().searchInsert(nums, target) == 1


def test_case_3():
    nums = [1, 3]
    target = 0
    assert Solution().searchInsert(nums, target) == 0


def test_case_4():
    nums = [1, 3]
    target = 1
    assert Solution().searchInsert(nums, target) == 0
