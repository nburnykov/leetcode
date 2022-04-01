from typing import List


def threeSum2(nums: List[int]) -> List[List[int]]:
    """
    N invocations of two sum algo, hash map without sorting
    :param nums:
    :return:
    """
    result = []
    for i in range(len(nums) - 2):  # 2 - extra space for j and k components
        v = nums[i]
        num_hash = set()
        for j in range(i + 1, len(nums) - 1):
            if -(v + nums[j]) in num_hash:
                result.append([v, -(v + nums[j]), nums[j]])
            else:
                num_hash.add(nums[j])

    return result


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    N invocations of two sum algo, sorting without hashmap
    :param nums:
    :return:
    """
    nums.sort()
    result = []
    prev_n = None

    for i in range(len(nums) - 2):
        if nums[i] == prev_n:  # avoid unnecessarily operations
            continue

        prev_n = nums[i]

        start = i + 1
        end = len(nums) - 1

        while start < end:
            summ = nums[i] + nums[start] + nums[end]
            if summ == 0:
                r = [nums[i], nums[start], nums[end]]
                if len(result) > 0:
                    if result[-1] != r:
                        result.append(r)
                else:
                    result.append(r)
            if summ > 0:
                end -= 1
            else:
                start += 1

    return list(result)