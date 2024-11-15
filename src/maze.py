# Class to handle the maze itself
from window import *
from cell import *
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.path = []
        self.successful_path = []
        if seed == None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed
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
    def _draw_cell(self, i, j, animate=False):
        self.cells[i][j].draw()
        if animate == True:
            self._animate()


    # Helper method for _draw_cell. sleeps 0.05 secs to allow us to visually see whats happening on the GUI
    def _animate(self, solve=False, undo=False):
        self.win.redraw()
        if solve == True:
            time.sleep(0.05)
        if undo == True:
            time.sleep(0.1)
        time.sleep(0.01)

    # The maze will always start at 0,0 and end at either the end of a column or row on the bottom or right side
    def _break_entrance_and_exit(self):
        # get random int to determine which wall will be broken to start
        start = random.randint(0, 1)
        end = random.randint(0, 1)

        # start (top left) cell logic
        if start == 0:
            self.cells[0][0].has_left_wall = False
        else:
            self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0, animate=True)
        
        # end (bottom right) cell logic
        if end == 0:
            #pick a row to make the end cell
            row = random.randint(0, len(self.cells[0]) - 1)
            self.cells[-1][row].has_right_wall = False
            self.end = self.cells[-1][row]
            self._draw_cell(-1, row, animate=True)
        else:
            # pick a column to make the end cell
            col = random.randint(0, len(self.cells) - 1)
            self.cells[col][-1].has_bottom_wall = False
            self.end = self.cells[col][-1]
            self._draw_cell(col, -1, animate=True)


    # Depth first cell traversal to create maze
    def _break_walls_r(self, i, j):
        # Set visited status to True for current cell
        cell = self.cells[i][j]
        cell.visited = True
        
        while True:
            # initialize list of unvisited neighboring cells
            to_visit = []

            #check adjacent cells visited status and append to list if unvisited
            if i > 0:
                left_cell = self.cells[i - 1][j]
                if left_cell.visited == False:
                    to_visit.append(left_cell)
            if j > 0:
                top_cell = self.cells[i][j - 1]
                if top_cell.visited == False:
                    to_visit.append(top_cell)
            if i < self.num_cols - 1:
                right_cell = self.cells[i + 1][j]
                if right_cell.visited == False:
                    to_visit.append(right_cell)
            if j < self.num_rows - 1:
                bottom_cell = self.cells[i][j + 1]
                if bottom_cell.visited == False:
                    to_visit.append(bottom_cell)
            # If there is no where to go, draw the cell and break the loop    
            if len(to_visit) == 0:
                self._draw_cell(i, j, animate=True)
                return
            else:
                # otherwise, pick a random direction, then break the walls between the cells, then recursively call this funciton on the next cell
                index = random.randint(0, len(to_visit) - 1)
                if i > 0:
                    if to_visit[index] == left_cell:
                        left_cell.has_right_wall = False
                        cell.has_left_wall = False
                        self._break_walls_r(i - 1, j)
                        self._draw_cell(i, j, animate=True)
                        continue
                if j > 0:
                    if to_visit[index] == top_cell:
                        top_cell.has_bottom_wall = False
                        cell.has_top_wall = False
                        self._break_walls_r(i, j - 1)
                        self._draw_cell(i, j, animate=True)
                        continue
                if i < self.num_cols - 1:
                    if to_visit[index] == right_cell:
                        right_cell.has_left_wall = False
                        cell.has_right_wall = False
                        self._break_walls_r(i + 1, j)
                        self._draw_cell(i, j, animate=True)
                        continue
                if j < self.num_rows - 1:
                    if to_visit[index] == bottom_cell:
                        bottom_cell.has_top_wall = False
                        cell.has_bottom_wall = False
                        self._break_walls_r(i, j + 1)
                        self._draw_cell(i, j, animate=True)
                        continue

    # method to reset cell.visited status for the maze solving step
    def _reset_cell_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    # solve method calls _solve_r and returns True if maze solved and False if not
    def solve(self):
        solved = self._solve_r(0, 0)
        self.path = []
        if solved == True:
            self._animate_solution_path()
            return True
        else:
            return False

    # run solving algor
    def _solve_r(self, i, j, search_type="Depth First"):
        if search_type == "Depth First":
            solved = self._depth_first(i, j)
            if solved == True:
                return True
            else:
                return False

    # depth first solving algorithm
    def _depth_first(self, i, j):
        cell = self.cells[i][j]
        cell.visited = True
        self.path.append(cell)
        if cell == self.end:
            # Record the successful path
            self.successful_path = list(self.path)
            return True
        #check adjacent cells visited status and if it has a wall between current cell and it. If there is no wall and the cell is unvisted it draws a move in red then calls _depth_first on the next cell. If True return True, else draw undo move.
        if j < self.num_rows - 1:
            bottom_cell = self.cells[i][j + 1]
            if bottom_cell.visited == False:
                if bottom_cell.has_top_wall == False:
                    cell.draw_move(bottom_cell)
                    self._animate(solve=True)
                    solved = self._depth_first(i, j + 1)
                    if solved == True:
                        return True
                    else:
                        cell.draw_move(bottom_cell, undo=True)
                        self._animate(undo=True)
        if i < self.num_cols - 1:
            right_cell = self.cells[i + 1][j]
            if right_cell.visited == False:
                if right_cell.has_left_wall == False:
                    cell.draw_move(right_cell)
                    self._animate(solve=True)
                    solved = self._depth_first(i + 1, j)
                    if solved == True:
                        return True
                    else:
                        cell.draw_move(right_cell, undo=True)
                        self._animate(undo=True)
        if i > 0:
            left_cell = self.cells[i - 1][j]
            if left_cell.visited == False:
                if left_cell.has_right_wall == False:
                    cell.draw_move(left_cell)
                    self._animate(solve=True)
                    solved = self._depth_first(i - 1, j)
                    if solved == True:
                        return True
                    else:
                        cell.draw_move(left_cell, undo=True)
                        self._animate(undo=True)
        if j > 0:
            top_cell = self.cells[i][j - 1]
            if top_cell.visited == False:
                if top_cell.has_bottom_wall == False:
                    cell.draw_move(top_cell)
                    self._animate(solve=True)
                    solved = self._depth_first(i, j - 1)
                    if solved == True:
                        return True
                    else:
                        cell.draw_move(top_cell, undo=True)
                        self._animate(undo=True)
        self.path.pop()
        return False

    def _animate_solution_path(self):
        if not self.successful_path:
            print("No successful path found for animation.")
            return
    
        for i in range(len(self.successful_path) - 1):
            cell = self.successful_path[i]
            next_cell = self.successful_path[i + 1]
            cell.draw_move(next_cell, solved=True)
            self._animate()