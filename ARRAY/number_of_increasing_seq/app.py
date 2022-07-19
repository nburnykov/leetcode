###########################################################################################
# leetcode problem  https://leetcode.com/problems/number-of-longest-increasing-subsequence/
###########################################################################################
import bisect
from typing import List


def binary_search(arr: List[int], target: int, left: bool = True) -> int:
    if target > arr[-1]:
        return len(arr)
    if target < arr[0]:
        return 0

    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid - 1] < target < arr[mid]:
            return mid
        if arr[mid] == target:
            return mid if left else mid + 1
        if target > arr[mid]:
            l = l + 1
        else:
            r = r - 1


def findNumberOfLIS(nums: List[int]) -> int:
    """
    Patience sort approach
    """
    stacks, stack_mins, lis_count = [[float("inf")]], [float("-inf")], [[0, 1]]
    for n in nums:
        if n > stack_mins[-1]:
            idx = binary_search(stacks[-1], -n, left=False)
            lis = lis_count[-1][-1] - lis_count[-1][idx]
            lis_count.append([0, lis])
            stacks.append([-n])
            stack_mins.append(n)
        else:
            idx = binary_search(stack_mins, n)
            lis_idx = binary_search(stacks[idx - 1], -n, left=False)
            lis = lis_count[idx - 1][-1] - lis_count[idx - 1][lis_idx]
            lis_count[idx].append(lis_count[idx][-1] + lis)
            stack_mins[idx] = n
            stacks[idx].append(-n)

    return lis_count[-1][-1]

def findNumberOfLIS1(nums):
    if not nums: return 0

    decks, ends_decks, paths = [], [], []
    for num in nums:
        deck_idx = bisect.bisect_left(ends_decks, num)
        n_paths = 1
        if deck_idx > 0:
            l = bisect.bisect(decks[deck_idx - 1], -num)
            n_paths = paths[deck_idx - 1][-1] - paths[deck_idx - 1][l]

        if deck_idx == len(decks):
            decks.append([-num])
            ends_decks.append(num)
            paths.append([0, n_paths])
        else:
            decks[deck_idx].append(-num)
            ends_decks[deck_idx] = num
            paths[deck_idx].append(n_paths + paths[deck_idx][-1])

    return paths[-1][-1]