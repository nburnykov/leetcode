def isValid(s: str) -> bool:
    par = {'(': ')', '[': ']', '{': '}'}

    q = []
    for p in s:
        if len(q) > 0:
            if p == par.get(q[-1]):
                q.pop(-1)
                continue

        if p in '({[':
            q.append(p)
        else:
            return False

    return len(q) == 0