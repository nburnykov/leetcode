###########################################################################################
# leetcode problem https://leetcode.com/problems/combination-sum/
###########################################################################################

from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    q = [([], sorted(candidates), target)]
    result = []
    while len(q) > 0:
        path, cand, t = q.pop(-1)
        if t == 0:
            result.append(path)
        if t > 0:
            for i in range(0, len(cand)):
                if i > 0 and cand[i] == cand[i - 1]:
                    continue
                p = path + [cand[i]]
                t_new = t - cand[i]
                q.append((p, cand[i + 1:], t_new))

    return result
