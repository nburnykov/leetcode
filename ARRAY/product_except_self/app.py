from typing import List


def productExceptSelf_my(nums: List[int]) -> List[int]:
    prod = 1
    zero_count = 0
    for n in nums:
        if n != 0:
            prod = 1 if prod == 0 else prod
            prod *= n
        else:
            zero_count += 1
    result = []
    for n in nums:
        if n != 0:
            if zero_count == 0:
                result.append(prod // n)
            else:
                result.append(0)
        else:
            if zero_count < 2:
                result.append(prod)
            else:
                result.append(0)
    return result


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    The idea is to calculate product of the right and left part of sequence for every i

    1 5 64 i 8 7 12
    right  ^   left

    """
    if nums == [0]:
        return nums

    result = [1 for _ in nums]
    right = 1
    left = 1

    for i in range(len(nums)):
        result[i] *= left
        result[-1 - i] *= right

        left *= nums[i]
        right *= nums[-1 - i]

    return result
