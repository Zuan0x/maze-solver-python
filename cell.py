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
        self.visited = False

    def draw(self, canvas):
        line_color = "#111"
        no_line_color = "#FFF"

        canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill= line_color if self.has_left_wall else no_line_color, width=2)
        canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill= line_color if self.has_top_wall else no_line_color, width=2)
        canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill= line_color if self.has_right_wall else no_line_color, width=2)
        canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill= line_color if self.has_bottom_wall else no_line_color, width=2)

    def draw_move(self, to_cell, canvas, undo=False):
        #draw a line from the center of one cell to another
        #If the undo flag is not set, the line you draw should be "red". Otherwise, make it "gray"
        line = Line(Point(self.x1 + (self.x2 - self.x1) / 2, self.y1 + (self.y2 - self.y1) / 2), Point(to_cell.x1 + (to_cell.x2 - to_cell.x1) / 2, to_cell.y1 + (to_cell.y2 - to_cell.y1) / 2), "#f00" if not undo else "#888")
        line.draw(canvas)

    def break_wall(self, wall):
        #set the appropriate wall to False
        if wall == 'left':
            self.has_left_wall = False
        elif wall == 'right':
            self.has_right_wall = False
        elif wall == 'top':
            self.has_top_wall = False
        elif wall == 'bottom':
            self.has_bottom_wall = False
