###########################################################################################
# leetcode problem https://leetcode.com/problems/longest-valid-parentheses/
###########################################################################################

def longestValidParentheses(s: str) -> int:
    """
    completed segment is like
    (()(())) - number of '(' = number of ')' and they are placed in valid order

    incomplete segment is like
    ((()()()(((()(((((((

    separated segments are like
    (completed))))(completed)
    """
    results = [0]  # to store the parentheses count in completed valid segments separated with excessive )
    ladder = []  # to store current incomplete segment
    for ch in s:
        if ch == '(':
            ladder.append(0)  # increase parentheses level
        if ch == ')':
            if len(ladder) > 1:  # segment incomplete
                c = ladder.pop(-1)  # decrease parentheses level
                ladder[-1] += c + 2
            elif len(ladder) == 1:  # segment completed but previous is also completed one - union (segment1)(segment2)
                c = ladder.pop(-1)
                results[-1] += c + 2
            else:  # excessive ) found, segments separated
                results.append(0) if results[-1] > 0 else None

    return max([*results, *ladder])  # maximum among all the separated segments and current (=last) incomplete one








