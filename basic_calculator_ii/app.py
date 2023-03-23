def calculate(s: str) -> int:
    s += "%"
    tokens = []
    number = ""
    last_operation = "+"
    for char in s:  # type: str
        if char == " ":
            continue
        if char.isnumeric():
            number += char
        else:
            number = int(number)
            if last_operation == "+":
                tokens.append(number)
            if last_operation == "-":
                tokens.append(-number)
            if last_operation == "*":
                tokens[-1] *= number
            if last_operation == "/":
                if tokens[-1] < 0:
                    tokens[-1] = -(-tokens[-1] // number)
                else:
                    tokens[-1] //= number
            last_operation = char
            number = ""

    return sum(tokens)
