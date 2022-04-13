from container_with_most_water.container_with_most_water import maxArea


def test_case_1():
    input = [1,8,6,2,5,4,8,3,7]
    output = 49
    assert maxArea(input) == output