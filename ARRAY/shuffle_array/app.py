###########################################################################################
# leetcode problem  https://leetcode.com/problems/shuffle-an-array/
###########################################################################################

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums.copy()

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        result = self.origin.copy()
        for i in range(0, len(result)):
            rand = random.randint(i, len(result) - 1)
            result[i], result[rand] = result[rand], result[i]

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()