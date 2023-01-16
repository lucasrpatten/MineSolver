"""
    Contains the necessary code to solve the the minesweeper from an array
"""

import numpy as np

small_game = np.array([["E", "E", "E", "E", "E", 1, "U", "U", "U", "U"],
                       ["E", "E", "E", "E", "E", 1, 2, 4, "U", "U"],
                       [1, 1, 1, "E", "E", "E", "E", 2, "U", "U"],
                       ["U", "U", 1, "E", "E", "E", "E", 1, 1, 1],
                       ["U", 2, 1, "E", "E", "E", "E", "E", "E", "E"],
                       ["U", 1, "E", "E", "E", "E", "E", "E", "E", "E"],
                       ["U", 1, 2, 1, 1, "E", "E", "E", 1, 1],
                       ["U", "U", "U", "U", 1, "E", "E", "E", 1, "U"]])


class Solver:
    """Contains methods to solve as much as possible
    """

    def __init__(self: object, mine_array: np.ndarray) -> None:
        self.mine_array = mine_array
        self.iterations = 0
        self.dimensions = self.mine_array.shape
        self.height = self.dimensions[0]
        self.width = self.dimensions[1]

    def solve_all_possible(self):
        """Solve every possible square with current data"""

    def flags_around(self, point) -> int:
        """Count the number of flags around a point"""

    def solve_around(self, row, col) -> None:
        point_value = self.mine_array[row, col]
        if not isinstance(point_value, int):
            return
        adjacent = self.neighbors(row, col)

    def neighbors(self, row, col):
        result = []
        for row_add in range(-1, 2):
            new_row = row + row_add
            if new_row >= 0 and new_row <= len(self.mine_array)-1:
                for col_add in range(-1, 2):
                    new_col = col + col_add
                    if new_col >= 0 and new_col <= len(self.mine_array)-1:
                        if new_col == col and new_row == row:
                            continue
                        result.append((self.mine_array[new_col][new_row], new_col, new_row))
        return result


a = Solver(small_game)
print(a.neighbors(5, 0))
