###########################################################################################
# leetcode problem  https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
###########################################################################################

def hasAllCodes(s: str, k: int) -> bool:
    # construct binary codes as strings
    codes = set()
    ln = 2 ** k

    for i in range(0, len(s) - k + 1):
        codes.add(s[i:i + k])

        if len(codes) == ln:  # we have all the possible codes
            return True

    return False
