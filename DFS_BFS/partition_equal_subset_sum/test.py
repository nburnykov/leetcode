from DFS_BFS.partition_equal_subset_sum.app import canPartition


def test_case_1():
    nums = [1, 5, 11, 5]
    assert canPartition(nums)


def test_case_2():
    nums = [1, 2, 3, 5]
    assert not canPartition(nums)
