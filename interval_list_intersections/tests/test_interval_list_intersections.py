from interval_list_intersections.interval_list_intersections import intervalIntersection


def test_case_1():
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    result = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    assert intervalIntersection(firstList, secondList) == result