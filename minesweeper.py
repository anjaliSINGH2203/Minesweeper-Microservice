
```
import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = []
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        mines_left = self.mines
        while mines_left > 0:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.grid[row][col] != 'M':
                self.grid[row][col] = 'M'
                self.mine_positions.append((row, col))
                mines_left -= 1

    def _calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 'M':
                    continue
                count = 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 'M':
                            count += 1
                self.grid[row][col] = str(count) if count > 0 else ' '

    def get_grid(self):
        return self.grid
      ```
