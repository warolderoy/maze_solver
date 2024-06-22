from graphics import Point, Line

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)

        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)

        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)

        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)
        
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)
        
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"
        
        if self._x1 == None:
            raise Exception("cell not drawn")
        if to_cell._x1 == None:
            raise Exception("to_cell not drawn")
        
        p1 = Point((self._x1+self._x2)//2, (self._y1+self._y2)//2)
        p2 = Point((to_cell._x1+to_cell._x2)//2, (to_cell._y1+to_cell._y2)//2)

        self._win.draw_line(Line(p1, p2), line_color)
