# Class file for the GUI Window


from tkinter import Tk, BOTH, Canvas
from line import *
from point import *

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.minsize(self.width, self.height)


# Tkinter requires manual redrawing
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

# method to keep the window going until closed    
    def wait_for_close(self):
        self.is_running = True

        while self.is_running == True:
            self.redraw()

        print("<----------Window closed---------->")

# method to force the code to stop when the window is closed when partnered with the logic in the constructor
    def close(self):
        self.is_running = False

# method to draw lines, takes a line object and a fill color and calls the line object's draw() method
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)