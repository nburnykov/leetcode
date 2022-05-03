def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    nx = x
    result = 0
    while x > 0:
        d = x % 10
        x //= 10
        result = result * 10 + d

    return nx == result