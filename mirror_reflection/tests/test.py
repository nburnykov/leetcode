from mirror_reflection.app import mirrorReflection


def test_case_1():
    p = 2
    q = 1
    r = 2
    assert mirrorReflection(p, q) == r


def test_case_2():
    p = 3
    q = 1
    r = 1
    assert mirrorReflection(p, q) == r