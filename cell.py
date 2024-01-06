import random
from graphics import Window, Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, canvas):
        if self.has_left_wall:
            canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="#f00", width=2)
        if self.has_right_wall:
            canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="#f00", width=2)
        if self.has_top_wall:
            canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="#f00", width=2)
        if self.has_bottom_wall:
            canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="#f00", width=2)
    
    def draw_move(self, to_cell, canvas, undo=False):
        #draw a line from the center of one cell to another
        #If the undo flag is not set, the line you draw should be "red". Otherwise, make it "gray"
        line = Line(Point(self.x1 + (self.x2 - self.x1) / 2, self.y1 + (self.y2 - self.y1) / 2), Point(to_cell.x1 + (to_cell.x2 - to_cell.x1) / 2, to_cell.y1 + (to_cell.y2 - to_cell.y1) / 2), "#f00" if not undo else "#888")
        line.draw(canvas)


