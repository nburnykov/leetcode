from partition_label.app import partitionLabels


def test_case_1():
    s = "ababcbacadefegdehijhklij"
    r = [9, 7, 8]
    assert partitionLabels(s) == r


def test_case_2():
    s = "eccbbbbdec"
    r = [10]
    assert partitionLabels(s) == r


def test_case_3():
    s = "a"
    r = [1]
    assert partitionLabels(s) == r
