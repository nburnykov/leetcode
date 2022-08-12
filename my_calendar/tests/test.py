from my_calendar.app import MyCalendar


def test_case_1():
    mc = MyCalendar()
    assert mc.book(10, 20)
    assert not mc.book(15, 25)
    assert mc.book(20, 30)


def test_case_2():
    mc = MyCalendar()
    bookings = [[47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]]
    results = [True, True, False, False, True, False, True, True, True, False]
    for b, r in zip(bookings, results):
        assert mc.book(b[0], b[1]) == r
