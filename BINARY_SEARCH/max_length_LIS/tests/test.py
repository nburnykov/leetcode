from BINARY_SEARCH.max_length_LIS.app import lengthOfLIS, insert_element, Chain


def test_case_1():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    r = 4
    assert lengthOfLIS(nums) == r

def test_case_2():
    nums = [0, 1, 0, 3, 2, 3]
    r = 4
    assert lengthOfLIS(nums) == r


def test_case_3():
    nums = [7,7,7,7,7,7]
    r = 1
    assert lengthOfLIS(nums) == r


def test_insert_1():
    ch = [1,2,4,6]
    i = 3
    r = [1, 2, 3, 6]
    assert insert_element(Chain(ch), i) == r


def test_insert_2():
    ch = [2]
    i = 1
    r = [1]
    assert insert_element(Chain(ch), i) == r

def test_insert_3():
    ch = [0, 1]
    i = 0
    r = [0, 1]
    assert insert_element(Chain(ch), i) == r