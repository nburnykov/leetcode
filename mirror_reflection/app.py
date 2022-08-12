###########################################################################################
# leetcode problem https://leetcode.com/problems/mirror-reflection/
###########################################################################################
from math import gcd


def mirrorReflection(p: int, q: int) -> int:
    """
    The idea id that we create a row of virtual rooms, in this case beam becomes a zigzag going through the row.
    """

    g = gcd(p, q)
    p, q = p // g, q // g

    if p % 2 == 0:
        return 2

    if q % 2 == 0:
        return 0

    return 1