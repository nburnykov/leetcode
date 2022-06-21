###########################################################################################
# leetcode problem  https://leetcode.com/problems/gray-code/
###########################################################################################

from typing import List


def grayCode(n: int) -> List[int]:
    """
    pattern:
    000
    001
    011
    010
    110
    111
    101
    100
    reverse current result on every step with the addition of leading 1
    """
    result = [0, 1]
    for i in range(1, n):
        for j in range(len(result) -1, -1, -1):  # reverse of the result
            result.append(result[j] | 1 << i)
    return result

