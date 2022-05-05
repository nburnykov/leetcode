###########################################################################################
# leetcode problem https://leetcode.com/problems/3sum-closest/
###########################################################################################

from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest, r = float('inf'), 0
    len_nums = len(nums)
    if len_nums < 4:
        return sum(nums)

    for i in range(len_nums - 2):
        j = i + 1
        k = len_nums - 1
        while j < k:
            if nums[i] + nums[j] > closest:  # early stopping
                break
            s = nums[i] + nums[j] + nums[k]
            d = s - target
            if abs(d) < closest:
                closest = abs(d)
                r = d + target
            if d == 0:
                return s
            if d > 0:
                k -= 1
            if d < 0:
                j += 1

    return r


def threeSumClosest2(nums: List[int], target: int) -> int:
    closest, s = float('inf'), 0
    len_nums = len(nums)
    if len_nums < 4:
        return sum(nums)

    for i in range(len_nums - 2):
        for j in range(i + 1, len_nums - 1):
            sum1 = nums[i] + nums[j]
            diff = abs(target - sum1)
            if closest < diff:
                continue
            for k in range(j + 1, len_nums):
                sum2 = sum1 + nums[k]
                diff = abs(target - sum2)
                if closest > diff:
                    closest, s = diff, sum2
    return s
