import time
import random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()

    def _create_cells(self):
        #fill a self._cells list with lists of cells. Each top-level list is a column of Cell objects. Once matrix is populated it should call its _draw_cell() method on each Cell.
        self.cells = []
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                col_cells.append(Cell(x1, y1, x2, y2))
            self.cells.append(col_cells) 
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(self.cells[i][j], i, j)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()

    def _draw_cell(self, cell, i, j):
        #calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself. The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        if self._win is None:
            return
        self.cells[i][j].draw(self._win.canvas)
        self._animate()
    
    def _break_entrance_and_exit(self):
        self.cells[0][0].break_wall('top')
        self._draw_cell(self.cells[0][0], 0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].break_wall('bottom')
        self._draw_cell(self.cells[self.num_cols - 1][self.num_rows - 1], self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        #recursively break walls until all cells have been visited
        self.cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(self, i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def _animate(self):
        time.sleep(0.01)
        if self._win is None:
            return
        self._win.redraw()

    def _solve(self):
        #solve the maze
        solved = self._solve_r(0, 0)

    def _solve_r(self, i, j):
        #recursively solve the maze
        #The _solve_r method returns True if the current cell is an end cell, OR if it leads to the end cell. It returns False if the current cell is a loser cell.
        
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        #For each direction
        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j], self._win.canvas)
            if self._solve_r(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], self._win.canvas, True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self.num_cols - 1
            and not self.cells[i][j].has_right_wall
            and not self.cells[i + 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j], self._win.canvas)
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], self._win.canvas, True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self.cells[i][j].has_top_wall
            and not self.cells[i][j - 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1], self._win.canvas)
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], self._win.canvas, True)

        # move down if there is no wall and it hasn't been visited      
        if (
            j < self.num_rows - 1
            and not self.cells[i][j].has_bottom_wall
            and not self.cells[i][j + 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1], self._win.canvas)
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], self._win.canvas, True)

        return False
