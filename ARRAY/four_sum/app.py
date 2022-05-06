###########################################################################################
# leetcode problem https://leetcode.com/problems/4sum/
###########################################################################################

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    len_nums = len(nums)

    if len_nums < 4:
        return []

    result = []
    c = set()
    for i in range(len_nums - 3):
        for j in range(i + 1, len_nums - 2):
            st = nums[i] + nums[j]
            k = j + 1
            l = len_nums - 1
            while k < l:
                d = st + nums[k] + nums[l] - target
                if d == 0:
                    r = [nums[i], nums[j], nums[k], nums[l]]
                    k += 1
                    if tuple(r) not in c:
                        c.add(tuple(r))
                        result.append(r)

                if d > 0:
                    l -= 1
                if d < 0:
                    k += 1

    return result
