#Main File for the program

from window import *
from cell import *
from maze import *

def main():
    # Initialize the window
    win = Window(800, 600)

    maze = Maze(10, 10, 20, 30, 50, 50, win)
    print("Creating Grid...")
    maze._create_cells()
    print("Generating maze...")
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cell_visited()
    print("Running Depth First algorithm to solve the maze...")
    maze.solve()

    # Keep the window open until closed by the user
    win.wait_for_close()


main()