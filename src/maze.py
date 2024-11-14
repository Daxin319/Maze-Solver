# Class to handle the maze itself
from window import *
from cell import *
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    # Creates the maze matrix and draws it
    def _create_cells(self):
        self.cells = []
        x1 = self.x1
        for i in range(self.num_cols):
            cols = []
            y1 = self.y1
            for j in range(self.num_rows):
                top_left = Point(x1, y1)
                bottom_right = Point(x1 + self.cell_size_x, y1 + self.cell_size_y)
                cell = Cell(self.win, top_left, bottom_right)
                cols.append(cell)
                y1 += self.cell_size_y
            self.cells.append(cols)
            x1 += self.cell_size_x

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    # Helper method for _create_cells
    def _draw_cell(self, i, j):
        self.cells[i][j].draw()
        self._animate()

    # Helper method for _draw_cell. sleeps 0.05 secs to allow us to visually see whats happening on the GUI
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    # The maze will always start at 0,0 and end at self.win.width, self.win.height
    def _break_entrance_and_exit(self):
        # get random int to determine which wall will be broken to start
        start = random.randint(0, 1)
        end = random.randint(0, 1)

        # start (top left) cell logic
        if start == 0:
            self.cells[0][0].has_left_wall = False
        else:
            self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        # end (bottom right) cell logic
        if end == 0:
            self.cells[-1][-1].has_right_wall = False
        else:
            self.cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)