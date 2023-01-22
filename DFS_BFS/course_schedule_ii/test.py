from DFS_BFS.course_schedule_ii.app import findOrder


def test_case_1():
    numCourses = 2
    prerequisites = [[1, 0]]
    result = [0, 1]
    assert findOrder(numCourses, prerequisites) == result


def test_case_2():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result1 = [0, 1, 2, 3]
    result2 = [0, 2, 1, 3]
    r = findOrder(numCourses, prerequisites)
    assert r == result1 or r == result2


def test_case_3():
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    result = []
    assert findOrder(numCourses, prerequisites) == result


def test_case_4():
    numCourses = 3
    prerequisites = [[2, 1], [1, 0]]
    result = [0, 1, 2]
    assert findOrder(numCourses, prerequisites) == result
