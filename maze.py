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
            win
    ):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cel_size_y = cell_size_y
        self.__win = win

        self.__create_cells()


    def __create_cells(self):
        for _ in range(self.__num_cols):
            col = []
            for _ in range(self.__num_rows):
                cell = Cell(self.__win)
                col.append(cell)
            self.__cells.append(col)
        
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        x_offset = i * self.__cell_size_x + self.__x1
        y_offset = j * self.__cel_size_y + self.__y1

        self.__cells[i][j].draw(
            x_offset,
            y_offset,
            x_offset + self.__cell_size_x,
            y_offset + self.__cel_size_y
        )

        self.__animate()
    
    def __animate(self):
        self.__win.redraw()
        sleep(0.05)
        