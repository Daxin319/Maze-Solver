# Class for lines in the maze, takes 2 point objects as input

from window import *
from point import *

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

# function to draw lines, takes a canvas and a fill color. the fill color is a string "black", "red", etc.
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)