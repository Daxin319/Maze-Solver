#Main File for the program

from window import *
from cell import *
from maze import *

def main():
    # Initialize the window
    win = Window(800, 600)

    # Create a few cells to test
    # Create cells of 100x100 size starting at different positions
    p1_cell1 = Point(50, 50)    # Top-left corner of the first cell
    p2_cell1 = Point(150, 150)  # Bottom-right corner of the first cell
    cell1 = Cell(win, p1_cell1, p2_cell1)

    p1_cell2 = Point(160, 50)   # Top-left corner of the second cell
    p2_cell2 = Point(260, 150)  # Bottom-right corner of the second cell
    cell2 = Cell(win, p1_cell2, p2_cell2)

    p1_cell3 = Point(50, 160)   # Top-left corner of the third cell
    p2_cell3 = Point(150, 260)  # Bottom-right corner of the third cell
    cell3 = Cell(win, p1_cell3, p2_cell3)

    p1_cell4 = Point(160, 160)  # Top-left corner of the fourth cell
    p2_cell4 = Point(260, 260)  # Bottom-right corner of the fourth cell
    cell4 = Cell(win, p1_cell4, p2_cell4)

    # Draw the cells
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    # Draw moves between cells
    # Draw a move from cell1 to cell2 (should be a red line)
    cell1.draw_move(cell2, undo=False)

    # Draw a move from cell2 to cell4 (should be a red line)
    cell2.draw_move(cell4, undo=False)

    # Draw a move from cell4 to cell3 (should be a red line)
    cell4.draw_move(cell3, undo=False)

    # Draw a move back from cell3 to cell1 (should be a grey line to represent an undo)
    cell3.draw_move(cell1, undo=True)

    # Keep the window open until closed by the user
    win.wait_for_close()


main()