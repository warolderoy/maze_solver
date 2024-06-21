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

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y,
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
    
    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)

        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)

        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self.__win.draw_line(left_wall)

        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self.__win.draw_line(right_wall)
        
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self.__win.draw_line(top_wall)
        
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self.__win.draw_line(bottom_wall)
