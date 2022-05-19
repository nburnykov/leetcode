def countAndSay(n: int) -> str:
    if n == 1:  # base case
        return "1"
    else:
        result = countAndSay(n-1)
        counter = []
        for r in result:
            if len(counter) == 0 or counter[-1][0] != r:
                counter.append([r, 0])
            counter[-1][1] += 1
        result = ""
        for c in counter:
            result += str(c[1]) + c[0]
        return result

