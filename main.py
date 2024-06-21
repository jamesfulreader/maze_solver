from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_right_w = False
    c1.draw(50,50,100,100)

    c2 = Cell(win)
    c2.has_left_w = False
    c2.has_bottom_w = False
    c2.draw(100, 50, 100, 50)
    
    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_w = False
    c3.has_right_w = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_w = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    win.wait_for_close()

main()