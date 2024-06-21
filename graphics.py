from tkinter import Tk, BOTH, Canvas
# Remember to use python 3.10 to call

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(
            master=self.__root,
            bg="white",
            height=height,
            width=width
        )
        self.__canvas.pack(
            fill=BOTH,
            expand=1
        )
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        
        while self.__running:
            self.redraw()
        print("Window closed successfully")
    
    def close(self):
        self.__running = False
