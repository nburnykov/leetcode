from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    temp = []
    while len(asteroids) > 0:
        candidate_left = asteroids.pop()
        if len(temp) == 0:
            temp.append(candidate_left)
            continue
        candidate_right = temp.pop()

        if candidate_left > 0 > candidate_right:  # cross course
            if candidate_left + candidate_right == 0:  # of the same mass but signs are different (mutual annihilation)
                continue
            if abs(candidate_left) > abs(candidate_right):
                asteroids.append(candidate_left)  # right annihilated
            else:
                temp.append(candidate_right)  # left annihilated
            continue

        temp.append(candidate_right)
        temp.append(candidate_left)

    while len(temp) > 0:
        asteroids.append(temp.pop())

    return asteroids