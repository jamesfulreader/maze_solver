from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_left_w = False
    c1.draw(50,50,100,100)
    c2 = Cell(win)
    c2.has_right_w = False
    c2.draw(300,300,250,250)
    
    win.wait_for_close()

main()