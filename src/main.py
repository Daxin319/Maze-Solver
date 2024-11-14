#Main File for the program

from window import *
from line import *
from point import *

def main():
    # Initialize the window
    win = Window(800, 600)
    
    # Create points for the lines
    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(300, 300)
    p4 = Point(100, 300)

    # Create lines using the points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    # Draw the lines on the window canvas
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "blue")
    win.draw_line(line4, "green")

    # Keep the window open until closed by the user
    win.wait_for_close()


main()