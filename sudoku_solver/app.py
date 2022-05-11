from typing import List


class SudokuSolver:
    def __init__(self, board = None):
        self.board = board

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def place_in_row(self, candidate: str, row_num: int) -> bool:
        for item in self.board[row_num]:
            if candidate == item:
                return False
        return True

    def place_in_col(self, candidate: str, col_num: int) -> bool:
        for i in range(9):
            if candidate == self.board[i][col_num]:
                return False
        return True

    def place_in_square(self, candidate: str, row_num: int, col_num: int) -> bool:
        square_x = row_num // 3 * 3
        square_y = col_num // 3 * 3
        for x in range(square_x, square_x + 3):
            for y in range(square_y, square_y + 3):
                if self.board[x][y] == candidate:
                    return False
        return True

    def safe_to_place(self, candidate: str, row_num: int, col_num: int):
        return all([self.place_in_row(candidate, row_num),
                    self.place_in_col(candidate, col_num),
                    self.place_in_square(candidate, row_num, col_num)])

    def find_empty(self) -> (int, int):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == '.':
                    return x, y
        return None, None  # all cells are filled with numbers

    def solve(self):
        x, y = self.find_empty()
        if x is None:  # nothing to assign
            return True
        for n in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.safe_to_place(n, x, y):
                self.board[x][y] = n
                if self.solve():
                    return True
                else:
                    self.board[x][y] = '.'  # rollback change
        return False