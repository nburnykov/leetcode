from ARRAY.asteroid_collision.app import asteroidCollision


def test_case_1():
    asteroids = [5, 10, -5]
    result = [5, 10]
    assert asteroidCollision(asteroids) == result


def test_case_2():
    asteroids = [8, -8]
    result = []
    assert asteroidCollision(asteroids) == result


def test_case_3():
    asteroids = [10, 2, -5]
    result = [10]
    assert asteroidCollision(asteroids) == result


def test_case_4():
    asteroids = [-2, -1, 1, 2]
    result = [-2, -1, 1, 2]
    assert asteroidCollision(asteroids) == result
