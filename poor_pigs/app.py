import math


def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    iter = minutesToTest // minutesToDie
    return math.ceil(math.log(buckets, iter + 1) - 1e-15)