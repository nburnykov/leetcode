###########################################################################################
# leetcode problem  https://leetcode.com/problems/increasing-triplet-subsequence/
###########################################################################################

from typing import List


def increasingTriplet_first(nums: List[int]) -> bool:
    triplet = [float("-inf")]
    triplet_two = [float("-inf")]

    for n in nums:
        if len(triplet) > 1 and triplet[-2] < n < triplet[-1]:
            triplet[-1] = n
        if n > triplet[-1]:
            triplet.append(n)
        elif n > triplet_two[-1]:
            triplet_two.append(n)
        elif n < triplet_two[-1]:
            triplet_two[-1] = n

        if len(triplet_two) == len(triplet):
            triplet = triplet_two[:]
            triplet_two = [float("-inf")]

        if len(triplet) > 3:
            return True
    return False


def increasingTriplet(nums: List[int]) -> bool:
    one, two = float("inf"), float("inf")
    for n in nums:
        if n <= one:
            one = n
        elif n <= two:
            two = n
        elif n > two:
            return True
        else:
            pass
    return False
