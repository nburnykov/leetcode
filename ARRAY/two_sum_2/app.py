from typing import List

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


