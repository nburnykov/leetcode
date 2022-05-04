from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    negative_squares = []
    result = []
    for n in nums:
        n_2 = n * n
        if n < 0:
            negative_squares.append(n_2)
        if n >= 0:
            candidate = negative_squares[-1] if negative_squares else None
            while (candidate is not None) and (candidate < n_2):
                result.append(candidate)
                negative_squares.pop(-1)
                candidate = negative_squares[-1] if negative_squares else None
            result.append(n_2)

    result.extend(negative_squares[::-1])

    return result