from ARRAY.sliding_window_median.app import medianSlidingWindow


def test_case_1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    r = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
    assert medianSlidingWindow(nums, k) == r


def test_case_2():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    r = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
    assert medianSlidingWindow(nums, k) == r


def test_case_3():
    nums = [1]
    k = 1
    r = [1]
    assert medianSlidingWindow(nums, k) == r


def test_case_4():
    nums = [1, 1, 1, 1]
    k = 2
    r = [1, 1, 1]
    assert medianSlidingWindow(nums, k) == r


def test_case_5():
    nums = [4, 1, 7, 1, 8, 7, 8, 7, 7, 4]
    k = 4
    r = [2.50000, 4.00000, 7.00000, 7.50000, 7.50000, 7.00000, 7.00000]
    assert medianSlidingWindow(nums, k) == r
