###########################################################################################
# leetcode problem https://leetcode.com/problems/permutation-in-string/
###########################################################################################

def checkInclusion(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)
    refer = dict()
    for char in s1:
        refer[char] = refer.get(char, 0) + 1

    if len_s1 > len_s2:
        return False

    substr = dict()
    for i in range(-len_s1, len_s2 - len_s1):
        in_element = s2[i + len_s1]
        substr[in_element] = substr.get(in_element, 0) + 1
        out_element = s2[i] if i >= 0 else None
        if out_element:
            count = substr[out_element]
            if count > 1:
                substr[out_element] = substr[out_element] - 1
            else:
                substr.pop(out_element)

        if substr == refer:
            return True

    return False
