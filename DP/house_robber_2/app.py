from typing import List


def rob(nums: List[int]) -> int:
    def dp(nms: List[int]):
        for i in range(len(nms) - 3, -1, -1):
            nms[i] = max(nms[i + 1], nms[i + 2] + nms[i])
        return nms[0]

    if len(nums) == 0:  # corner cases
        return 0

    if len(nums) < 3:
        return max(nums)

    nums.append(0)
    r1 = dp(nums[1:])
    nums.pop(-1)
    nums[-1] = 0
    r2 = dp(nums)

    return max(r1, r2)
