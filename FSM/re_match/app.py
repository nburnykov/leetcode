###########################################################################################
# leetcode problem https://leetcode.com/problems/regular-expression-matching
###########################################################################################

def fsm(pattern: str) -> (dict, set):
    fsm_ = dict()
    current_states = [-1]  # initial open state
    for i in range(len(pattern)):
        if pattern[i] == '*':
            continue
        state = current_states[-1] + 1
        for s in current_states:  # close all open states
            fsm_.setdefault((s, pattern[i]), set()).add(state)
        if i < len(pattern) - 1 and pattern[i + 1] == '*':
            fsm_.setdefault((state, pattern[i]), set()).add(state)  # cycle
            current_states.append(state)  # register new open state
        else:
            current_states = [state]

    current_states = set(current_states)  # remove initial state
    if -1 in current_states:
        current_states.remove(-1)

    return fsm_, current_states


def isMatch(s: str, p: str) -> bool:
    fsm_, fs = fsm(p)

    current_states = {-1}
    for c in s:
        new_states = set()
        for cs in current_states:
            new_states.update(fsm_.get((cs, c), set()))
            new_states.update(fsm_.get((cs, '.'), set()))
        current_states = new_states

    return len(current_states & fs) > 0

