from binary_search.binary_search import Solution


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = Solution().search(nums, target)
    assert result == 4


def test_case_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = Solution().search(nums, target)
    assert result == -1


def test_case_3():
    nums = [2, 5]
    target = 2
    result = Solution().search(nums, target)
    assert result == 0


def test_case_4():
    nums = [-1, 0, 3, 5, 9, 12]
    target = -1
    result = Solution().search(nums, target)
    assert result == 0


def test_case_5():
    nums = [2, 5]
    target = 5
    result = Solution().search(nums, target)
    assert result == 1