from ARRAY.longest_common_prefix.app import longestCommonPrefix


def test_case_1():
    strs = ["flower", "flow", "flight"]
    r = "fl"
    assert longestCommonPrefix(strs) == r

def test_case_2():
    strs = ["a"]
    r = "a"
    assert longestCommonPrefix(strs) == r