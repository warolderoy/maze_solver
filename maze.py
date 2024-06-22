import random

from cell import Cell
from time import sleep

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cel_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)
        else:
            random.seed()

        self.__create_cells()
        if len(self._cells) > 0:
            if len(self._cells[0]) > 0:
                self._break_entrance_and_exit()
                self._break_walls_r(0, 0)


    def __create_cells(self):
        for _ in range(self._num_cols):
            col = []
            for _ in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        if self._win == None:
            return
        
        x_offset = i * self._cell_size_x + self._x1
        y_offset = j * self._cel_size_y + self._y1

        self._cells[i][j].draw(
            x_offset,
            y_offset,
            x_offset + self._cell_size_x,
            y_offset + self._cel_size_y
        )

        self.__animate()
    
    def __animate(self):
        if self._win == None:
            return
        
        self._win.redraw()
        sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self.__draw_cell(self._num_cols-1, self._num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            # Left
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append(tuple([i-1, j, "left"]))
            # Right
            if i < self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append(tuple([i+1, j, "right"]))
            # Top
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append(tuple([i, j-1, "top"]))
            # Bottom
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append(tuple([i, j+1, "bottom"]))
            
            if len(to_visit) == 0:
                return
            else:
                visiting = to_visit[random.randrange(len(to_visit))]
                if visiting[2] == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[visiting[0]][visiting[1]].has_right_wall = False
                elif visiting[2] == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[visiting[0]][visiting[1]].has_left_wall = False
                elif visiting[2] == "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[visiting[0]][visiting[1]].has_bottom_wall = False
                elif visiting[2] == "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[visiting[0]][visiting[1]].has_top_wall = False
                self.__draw_cell(i, j)

                self._break_walls_r(visiting[0], visiting[1])
        