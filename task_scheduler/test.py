from task_scheduler.app import leastInterval


def test_case_1():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    result = 8
    assert leastInterval(tasks, n) == result


def test_case_2():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    result = 6
    assert leastInterval(tasks, n) == result


def test_case_3():
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    result = 16
    assert leastInterval(tasks, n) == result


def test_case_4():
    tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "D", "E", "E", "E"]
    n = 2
    result = 12
    assert leastInterval(tasks, n) == result

def test_case_5():
    tasks = ["A","A","A","B","B","B", "C", "D", "D", "E"]
    n = 2
    result = 10
    assert leastInterval(tasks, n) == result

def test_case_6():
    tasks = ["A","A","A","E"]
    n = 2
    result = 7
    assert leastInterval(tasks, n) == result