from sort_colors.app import sortColors


def test_case_1():
    n = [4, 3, 4, 5, 6, 1]
    r = [1, 3, 4, 4, 5, 6]
    sortColors(n)
    assert tuple(n) == tuple(r)


def test_case_2():
    n = [2, 0, 2, 1, 1, 0]
    r = [0, 0, 1, 1, 2, 2]
    sortColors(n)
    assert tuple(n) == tuple(r)

def test_case_3():
    n = [2, 0, 1]
    r = [0, 1, 2]
    sortColors(n)
    assert tuple(n) == tuple(r)