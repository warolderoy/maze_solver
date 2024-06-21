from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)

    cell1.has_right_wall = False
    cell2.has_left_wall = False

    cell1.draw(0, 0, 100, 100)
    cell2.draw(100, 0, 200, 100)

    cell1.draw_move(cell2, True)
    
    win.wait_for_close()

main()