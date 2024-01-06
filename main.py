from tkinter import Tk, BOTH, Canvas

class Window (Tk):
    def __init__(self, width, height):
        Tk.__init__(self)
        self.title("Maze Solver")
        self.geometry("500x500")
        self.resizable(False, False)
        self.canvas = Canvas(self, width=width, height=width)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_rectangle(0, 0, width, height, fill="red")

        self.canvas.bind("<Button-1>", self.on_click)
        self.running = False

    def on_click(self, event):
        print("Clicked at", event.x, event.y)

    def redraw(self):
        #The redraw() method on the window class should simply call the root widget's update_idletasks() and update() methods. Each time this is called, the window will redraw itself.
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        #This method should set the data member we created to track the "running" state of the window to True. Next, it should call self.redraw() over and over as long as the running state remains True.
        self.running = True 
        while self.running:
            self.redraw()

    def close(self):
        # the close() method should simply set the running state to False. You'll also need to add another line to the constructor to call the protocol method on the root widget, to connect your close method to the "delete window" action. This will stop your program from running when you close the graphical window.
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
