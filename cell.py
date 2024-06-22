from graphics import Point, Line

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

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

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"
        
        if self.__x1 == None:
            raise Exception("cell not drawn")
        if to_cell.__x1 == None:
            raise Exception("to_cell not drawn")
        
        p1 = Point((self.__x1+self.__x2)//2, (self.__y1+self.__y2)//2)
        p2 = Point((to_cell.__x1+to_cell.__x2)//2, (to_cell.__y1+to_cell.__y2)//2)

        self.__win.draw_line(Line(p1, p2), line_color)
