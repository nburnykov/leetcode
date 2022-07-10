###########################################################################################
# leetcode problem https://leetcode.com/problems/valid-number/
###########################################################################################

def isNumber(s: str) -> bool:
    """
    A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.

    For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
    "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    """
    fsm = {
        (-1, '+-'): 0,
        (-1, '.'): 2,
        (-1, '09'): 1,
        (0, '09'): 1,
        (0, '.'): 2,
        (1, '.'): 2,
        (1, 'eE'): 4,
        (1, '09'): 1,
        (2, '09'): 3,
        (2, 'eE'): 4,
        (3, '09'): 3,
        (3, 'eE'): 4,
        (4, '+-'): 5,
        (4, '09'): 6,
        (5, '09'): 6,
        (6, '09'): 6,
    }
    final_states = {1, 2, 3, 6}
    current_state = -1
    state_passed = [current_state]

    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    plus_minus = {"+", "-"}
    e = {'e', 'E'}

    for c in s:
        new_state = None
        if c in digits:
            new_state = fsm.get((current_state, '09'))
        if c in plus_minus:
            new_state = fsm.get((current_state, '+-'))
        if c == '.':
            new_state = fsm.get((current_state, '.'))
        if c in e:
            new_state = fsm.get((current_state, 'eE'))
        if new_state is None:
            return False
        else:
            current_state = new_state
            state_passed.append(new_state)

    if current_state == 2:  # cannot be just . or -.  must include digit before dot
        return 1 in state_passed

    if current_state in {6, 7, 8}:
        return len({1, 3} & set(state_passed)) > 0

    return current_state in final_states