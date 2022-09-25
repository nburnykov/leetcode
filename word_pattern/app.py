###########################################################################################
# leetcode problem  https://leetcode.com/problems/word-pattern/submissions/
###########################################################################################

def wordPattern(pattern: str, s: str) -> bool:
    word_map = {}
    pattern_map = {}
    word_list = s.split()

    if len(word_list) != len(pattern):
        return False

    for p, w in zip(pattern, word_list):
        if w not in word_map and p not in pattern_map:
            word_map[w] = p
            pattern_map[p] = w
        else:
            pat = word_map.get(w)
            wrd = pattern_map.get(p)

            if (wrd, pat) != (w, p):
                return False

    return True