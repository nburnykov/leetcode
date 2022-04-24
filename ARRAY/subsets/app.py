from typing import List


def subsets2(nums: List[int]) -> List[List[int]]:
    n = len(nums) - 1
    result = [[]]
    for k in range(1, len(nums) + 1):
        indexes = []
        x = 0
        while True:
            if len(indexes) < k and x <= n:
                indexes.append(x)
                x += 1
            else:
                if indexes == list(range(n - k + 1, n + 1)):  # early stopping
                    break
                x = indexes.pop() + 1

            if len(indexes) == k:
                result.append([nums[i] for i in indexes])

    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for n in nums:
        result.extend([r + [n] for r in result])

    return result