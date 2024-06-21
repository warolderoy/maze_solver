from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(0, 0, 100, 100, win)
    cell2 = Cell(100, 0, 200, 100, win)

    cell1.has_right_wall = False
    cell2.has_left_wall = False

    cell1.draw()
    cell2.draw()
    
    win.wait_for_close()

main()