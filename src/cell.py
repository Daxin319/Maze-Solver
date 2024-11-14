# cell class handles individual cells in the maze

from window import *

class Cell():
    # Constructor takes a window and 2 point objects as input (the top left and bottom right corners)
    def __init__(self, window, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x1 = p1.x
        self.x2 = p2.x
        self.y1 = p1.y
        self.y2 = p2.y
        self.win = window.canvas
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self):

        #check if wall exists and draw if true
        if self.has_left_wall == True:
            # create corner not provided
            bottom_left = Point(self.x1, self.y2)
            #create wall line object
            left_wall = Line(self.p1, bottom_left)
            #draw the wall
            left_wall.draw(self.win)
        else:
            # create corner not provided
            bottom_left = Point(self.x1, self.y2)
            #create wall line object
            left_wall = Line(self.p1, bottom_left)
            #draw the wall
            left_wall.draw(self.win, "#d9d9d9")

        if self.has_top_wall == True:
            top_right = Point(self.x2, self.y1)
            top_wall = Line(self.p1, top_right)
            top_wall.draw(self.win)
        else:
            top_right = Point(self.x2, self.y1)
            top_wall = Line(self.p1, top_right)
            top_wall.draw(self.win, "#d9d9d9")

        if self.has_right_wall == True:
            top_right = Point(self.x2, self.y1)
            right_wall = Line(top_right, self.p2)
            right_wall.draw(self.win)
        else:
            top_right = Point(self.x2, self.y1)
            right_wall = Line(top_right, self.p2)
            right_wall.draw(self.win, "#d9d9d9")

        if self.has_bottom_wall == True:
            bottom_left = Point(self.x1, self.y2)
            bottom_wall = Line(bottom_left, self.p2)
            bottom_wall.draw(self.win)
        else:
            bottom_left = Point(self.x1, self.y2)
            bottom_wall = Line(bottom_left, self.p2)
            bottom_wall.draw(self.win, "#d9d9d9")

    # method draws a line from the center of self to another cell, red line if undo is false, grey if true for better mapping graphics
    def draw_move(self, to_cell, undo=False):
        # calculate center points and create line
        x1 = (self.x2 + self.x1) // 2
        y1 = (self.y2 + self.y1) // 2
        x2 = (to_cell.x2 + to_cell.x1) // 2
        y2 = (to_cell.y2 + to_cell.y1) // 2
        center_self = Point(x1, y1)
        center_to_cell = Point(x2, y2)
        path = Line(center_self, center_to_cell)
        # draw the line depending on undo state
        if undo == False:
            path.draw(self.win, "red", width=10)
        else:
            path.draw(self.win, "#d9d9d9", width=10)
            path.draw(self.win, "grey")