###########################################################################################
# leetcode problem  https://leetcode.com/problems/longest-increasing-subsequence/
###########################################################################################
from typing import List


def lengthOfLISDP(nums: List[int]) -> int:
    """
    A DP approach  O(n^2)
    nums:       7 5 1 3 1000 0 4 8 2
    lengths:    1 1 1 2 2    1 3 4 2  # max chain length ending with given number
    """
    lengths = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1

    return max(lengths)


class Chain:
    def __init__(self, l):
        self.c = l

    def append(self, el):
        self.c.append(el)

    def get(self, index):
        if len(self.c) == 0 or index < 0:
            return float("-inf")

        return self.c[index]

    def __len__(self):
        return len(self.c)

    def set(self, index, element):
        self.c[index] = element

    def last(self):
        if len(self.c) == 0:
            return float("-inf")
        else:
            return self.c[-1]

def insert_element(chain: Chain, element: int) -> List[int]:
    if chain.last() < element:
        chain.append(element)
        return chain.c
    l, r = 0, len(chain) - 1
    while l <= r:
        mid = (l + r) // 2
        if chain.get(mid-1) < element <= chain.get(mid):
            chain.set(mid, element)
            return chain.c
        if chain.get(mid - 1) >= element:
            r = mid - 1
            continue
        if chain.get(mid) < element:
            l = mid + 1
            continue

def lengthOfLIS(nums: List[int]) -> int:
    """
    Binary search approach
    save the longest chain and substitute corresponding elements with smaller nums if found
    """
    chain = Chain([])
    for n in nums:
        insert_element(chain, n)

    return len(chain)



