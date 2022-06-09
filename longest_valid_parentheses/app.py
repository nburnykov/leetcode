def longestValidParentheses(s: str) -> int:
    result = 0
    ladder = []
    for ch in s:
        if ch == '(':
            if len(ladder) == 0:
                ladder.append(1)
            else:
                ladder[-1] += 1
        if ch == ')':
            if len(ladder) > 1:
                if ladder[-1] % 2 != 0:  # opened sequence
                    ladder[-1] += 1
                else:
                    c = ladder.pop(-1)
                    ladder[-1] += c + 1
            if len(ladder) == 1:
                if ladder[-1] % 2 != 0:  # opened sequence
                    ladder[-1] += 1
                else:
                    c = ladder.pop(-1) + 1
                    result = max(result, c)








