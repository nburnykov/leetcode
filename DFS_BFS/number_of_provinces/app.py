from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    if len(isConnected) == 0:  # corner case
        return 0

    cities = set(range(len(isConnected)))
    result = 0
    while len(cities) > 0:
        q = [cities.pop()]  # DFS
        seen = set()
        while len(q) > 0:

            city = q.pop(-1)
            for i in range(0, len(isConnected)):
                if isConnected[city][i] == 1 and i not in seen:
                    seen.add(i)
                    q.append(i)

        cities -= seen
        result += 1

    return result