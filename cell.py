from graphics import Line, Point

class Cell:
    def __init__(self, window) -> None:
        self.has_left_w = True
        self.has_right_w = True
        self.has_top_w = True
        self.has_bottom_w = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_w:
            line = Line(Point(x1,y1), Point(x1,y2))
            self.__win.draw_line(line)
        
        if self.has_right_w:
            line = Line(Point(x1,y1), Point(x2,y1))
            self.__win.draw_line(line)

        if self.has_top_w:
            line = Line(Point(x2,y1), Point(x2,y2))
            self.__win.draw_line(line)
        
        if self.has_bottom_w:
            line = Line(Point(x1,y2), Point(x2,y2))
            self.__win.draw_line(line)