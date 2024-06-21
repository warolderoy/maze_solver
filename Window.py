from tkinter import Tk, BOTH, Canvas
# Remember to use python 3.10 to call

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(
            master=self.__root,
            height=height,
            width=width
        )
        self.canvas.pack()
        self.running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
