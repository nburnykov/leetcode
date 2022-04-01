from typing import List


def twoSumSlow(numbers: List[int], target: int) -> List[int]:  # n log n - slow solution
    for pointer_1, val_1 in enumerate(numbers):
        val_pair = target - val_1

        pivot_prev = pointer_1 + 1
        pivot = len(numbers) - 1

        while True:
            step = abs(pivot - pivot_prev) // 2
            if step == 0:
                step = 1

            if numbers[pivot] == val_pair:
                return [pointer_1 + 1, pivot + 1]

            if numbers[pivot - 1] < val_pair < numbers[pivot]:  # no solution for current val_1
                break

            if (numbers[pivot] < val_pair):
                pivot_prev = pivot
                pivot = pivot + step

                if pivot > len(numbers) - 1:
                    break
            else:
                pivot_prev = pivot
                pivot = pivot - step

                if pivot < 0:
                    break


def twoSum(numbers: List[int], target: int) -> List[int]:  # O(n) - optimal solution
    pointer_1 = 0
    pointer_2 = len(numbers) - 1
    while True:
        val_1 = numbers[pointer_1]
        val_2 = numbers[pointer_2]
        sum = val_1 + val_2
        if sum == target:
            return [pointer_1 + 1, pointer_2 + 1]

        if sum > target:
            pointer_2 -= 1

        if sum < target:
            pointer_1 += 1


