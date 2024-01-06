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

def main():
    win = Window(800, 600)
    win.draw_line(Point(0, 0), Point(800, 600), "#00f000")
    win.draw_line(Point(0, 600), Point(800, 0), "#00f")
    win.draw_line(Point(0, 0), Point(800, 0))
    win.draw_line(Point(0, 0), Point(0, 600))
    win.draw_line(Point(800, 0), Point(800, 600))
    win.draw_line(Point(0, 600), Point(800, 600))
    win.wait_for_close()


if __name__ == "__main__":
    main()
