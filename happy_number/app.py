def isHappy(n: int) -> bool:
    mem = set()
    while n not in mem:
        mem.add(n)
        s = 0

        n_last = n % 10
        while n_last != n:
            s += n_last * n_last
            n = n // 10
            n_last = n % 10

        s += n_last * n_last

        if s == 1:
            return True
        n = s

    return False
