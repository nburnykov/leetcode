from first_bad_version.first_bad_version import Solution


def test_case_1():
    s = Solution()
    s.BAD_VERSION = 4

    assert s.firstBadVersion(5) == s.BAD_VERSION


def test_case_2():
    s = Solution()
    s.BAD_VERSION = 1

    assert s.firstBadVersion(1) == s.BAD_VERSION


def test_case_3():
    s = Solution()
    s.BAD_VERSION = 2

    assert s.firstBadVersion(2) == s.BAD_VERSION

def test_case_4():
    s = Solution()
    s.BAD_VERSION = 1702766719

    assert s.firstBadVersion(2126753390) == s.BAD_VERSION
