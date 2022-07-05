from DFS_BFS.longest_consecutive_sequence.app import longestConsecutive


def test_case_1():
    nums = [100,4,200,1,3,2]
    r = 4
    assert longestConsecutive(nums) == r


def test_case_2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    r = 9
    assert longestConsecutive(nums) == r