###########################################################################################
# leetcode problem https://leetcode.com/problems/wildcard-matching/
###########################################################################################

def fsm(pattern: str) -> (dict, set):
    fsm_ = dict()
    current_states = [-1]
    for i in range(len(pattern)):
        state = current_states[-1] + 1
        p = '?' if pattern[i] == '*' else pattern[i]
        for cs in current_states:
            fsm_.setdefault((cs, p), set()).add(state)
        if pattern[i] == '*':
            fsm_.setdefault((state, '?'), set()).add(state)
            current_states.append(state)
        else:
            current_states = [state]

    return fsm_, set(current_states)


def isMatch(s: str, p: str) -> bool:
    fsm_, fs = fsm(p)
    states = {-1}
    for c in s:
        new_states = set()
        for st in states:
            new_states.update(fsm_.get((st, c), set()))
            new_states.update(fsm_.get((st, '?'), set()))
        states = new_states

    return len(states & fs) > 0
