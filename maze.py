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
            win = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cel_size_y = cell_size_y
        self._win = win

        self.__create_cells()


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
        