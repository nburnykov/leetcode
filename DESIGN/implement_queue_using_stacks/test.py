from DESIGN.implement_queue_using_stacks.app import MyQueue


def test_case_1():
    mq = MyQueue()
    mq.push(1)
    mq.push(2)
    assert mq.peek() == 1
    assert mq.pop() == 1
    assert not mq.empty()