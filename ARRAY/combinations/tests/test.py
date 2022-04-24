from ARRAY.combinations.app import combine


def test_case_1():

    n = 4
    k = 2
    output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert combine(n, k) == output


def test_case_2():

    n = 1
    k = 1
    output = [[1]]
    assert combine(n, k) == output


def test_case_3():
    n = 8
    k = 3
    output = [[1]]
    print(combine(n, k))