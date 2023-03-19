# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) > 0:
            _, min_val = self.mins[-1]
        else:
            min_val = float("inf")
        self.stack.append(val)
        if val < min_val:
            self.mins.append((len(self.stack), val))

    def pop(self) -> None:
        if self.mins[-1][0] == len(self.stack):
            self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1][1]
