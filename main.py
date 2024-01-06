from tkinter import Tk, BOTH, Canvas

class Window (Tk):
    def __init__(self, width, height):
        Tk.__init__(self)
        self.title("Maze Solver")
        self.geometry("500x500")
        self.resizable(False, False)
        self.canvas = Canvas(self, width=width, height=width)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_rectangle(0, 0, width, height, fill="white")

        self.canvas.bind("<Button-1>", self.on_click)
        self.running = False

    def on_click(self, event):
        print("Clicked at", event.x, event.y)

    def redraw(self):
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        self.running = True 
        while self.running:
            self.redraw()

    def close(self):       
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, start, end, color="#0f0"):
        line = Line(start, end, color)
        line.draw(self.canvas)
    
    def draw_cell(self, cell):
        cell.draw(self.canvas)
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end, color="#111111"):
        self.start = start
        self.end = end
        self.color = color

    def draw(self, canvas):
        print("Drawing line from", self.start.x, self.start.y, "to", self.end.x, self.end.y)
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color, width=2)

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

def main():
    win = Window(800, 600)
    win.draw_line(Point(0, 0), Point(800, 600), "#00f000")
    win.draw_line(Point(0, 600), Point(800, 0), "#00f")
    win.draw_cell(Cell(0, 0, 100, 100))
    win.wait_for_close()


if __name__ == "__main__":
    main()
