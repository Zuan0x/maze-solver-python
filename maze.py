import time
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

    def _animate(self):
        time.sleep(0.05)
        if self._win is None:
            return
        self._win.redraw()
