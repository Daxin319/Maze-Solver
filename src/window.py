# Class file for the GUI Window


from tkinter import Tk, BOTH, Canvas

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

################################################################################################################################################################################################################################

#Class to handle individual points in the maze. Takes two coordinates as input, x = 0 is the left side, y = 0 is the top of the window
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

################################################################################################################################################################################################################################

# Class for lines in the maze, takes 2 point objects as input
class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

# method to draw lines, takes a canvas and a fill color. the fill color is a string "black", "red", etc.
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)