###########################################################################################
# leetcode problem https://leetcode.com/problems/combination-sum-iii/
###########################################################################################
from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    q = [([], k, n)]
    result = []
    while len(q) > 0:
        comp, ln, t = q.pop(-1)
        if ln == 0 and t == 0:
            result.append(comp)
        if ln > 0 and t > 0:
            start_s = comp[-1] + 1 if len(comp) > 0 else 1
            for c in range(start_s, 10):
                t_new = t - c
                if t_new >= 0:
                    q.append((comp + [c], ln - 1, t_new))

    return result
