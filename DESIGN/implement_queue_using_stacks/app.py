# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def _move_to_output(self):
        if len(self.output) == 0:
            while len(self.input) > 0:
                self.output.append(self.input.pop())

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self._move_to_output()
        return self.output.pop()

    def peek(self) -> int:
        self._move_to_output()
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0