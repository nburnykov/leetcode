###########################################################################################
# leetcode problem https://leetcode.com/problems/combination-sum/
###########################################################################################

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    q = [([], candidates[:], target)]
    result = []
    while len(q) > 0:
        path, cand, t = q.pop(-1)
        if t == 0:
            result.append(path)
        if t > 0:
            for i in range(0, len(cand)):
                p = path + [cand[i]]
                t_new = t - cand[i]
                q.append((p, cand[i:], t_new))

    return result


