# https://leetcode.com/problems/minimum-window-substring
def minWindow(s: str, t: str) -> str:
    def t_in_s(s_map: dict, t_map: dict) -> bool:
        for t in t_map:
            if s_map.get(t, 0) < t_map[t]:
                return False
        return True

    min_lng = float("inf")
    min_str = ""

    p0, p1 = -1, -1
    t_map, s_map = {}, {}
    # build t_map
    for ch in t:
        t_map[ch] = t_map.get(ch, 0) + 1

    try:
        while True:
            if not t_in_s(s_map, t_map):  # expand window
                p1 += 1
                ch = s[p1]
                s_map[ch] = s_map.get(ch, 0) + 1
            else:  # shrink window
                p0 += 1
                ch = s[p0]
                s_map[ch] = s_map.get(ch, 0) - 1
                if p1 - p0 < min_lng:
                    min_lng = p1 - p0
                    min_str = s[p0:p1 + 1]
    except IndexError:
        return min_str
