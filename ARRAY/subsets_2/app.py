from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    result = [[]]
    seen = set()
    for n in sorted(nums):
        candidates = [r + [n] for r in result]
        for c in candidates:
            c_t = tuple(c)
            if c_t not in seen:
                seen.add(c_t)
                result.append(c)
    return result