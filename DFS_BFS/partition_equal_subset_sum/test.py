from DFS_BFS.partition_equal_subset_sum.app import canPartition


def test_case_1():
    nums = [1, 5, 11, 5]
    assert canPartition(nums)


def test_case_2():
    nums = [1, 2, 3, 5]
    assert not canPartition(nums)


def test_case_3():
    nums = [2, 2, 3, 5]
    assert not canPartition(nums)


def test_case_4():
    nums = [14, 9, 8, 4, 3, 2]
    assert not canPartition(nums)
