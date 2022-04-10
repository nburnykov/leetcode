from find_peak_element.find_peak_element import findPeakElement


def test_case_1():
    input = [1, 2, 3, 1]
    output = 2
    assert findPeakElement(input) == output


def test_case_2():
    input = [1, 2, 1, 3, 5, 6, 4]
    output = {1, 5}
    assert findPeakElement(input) in output


def test_case_3():
    input = [2, 1]
    output = 0
    assert findPeakElement(input) == output


def test_case_4():
    input = [3, 1, 2]
    output = {0, 2}
    assert findPeakElement(input) in output


def test_case_5():
    input = [1, 2]
    output = 1
    assert findPeakElement(input) == output