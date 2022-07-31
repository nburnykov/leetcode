###########################################################################################
# leetcode problem  https://leetcode.com/problems/bitwise-and-of-numbers-range/
###########################################################################################

def rangeBitwiseAnd(left: int, right: int) -> int:
    """
    000
    001 - 2
    ---
    010
    011
    ---
    ---
    100
    101
    ---
    110 - 6
    111

    the main idea here to find blocks crossing (the blocks are of sizes 2, 4, 8 e.t.c.). For example 2 and 6 are in
    neighbour blocks of size 4 and their bitwise AND result is 0 which is the start number of the block with left number.
    In case of 5 and 6 they are lie in neighbour blocks of size 2 and their result is 4 which is starting number of
    block with 5 and size of 2.
    """
    if left == right:
        return left
    divider = 2  # start with the smallest block size
    while right // divider - left // divider > 0:  # find the smallest block which has both numbers
        divider *= 2
    return left - left % (divider // 2)
