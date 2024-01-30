from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canv = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canv.pack(fill=BOTH, expand=1)
        self.__active = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__active = True
        while self.__active:
            self.redraw()

    def close(self):
        self.__active = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canv, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.one.x, self.one.y, self.two.x, self.two.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, win, wall_color="black"):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win
        self.wall_color = wall_color

    def draw(self, ptl, pbr):
        self.__x1 = ptl.x
        self.__y1 = ptl.y
        self.__x2 = pbr.x
        self.__y2 = pbr.y
        if self.has_left_wall:
            lw = Line(Point(ptl.x, ptl.y), Point(ptl.x, pbr.y))
            self.__win.draw_line(lw, self.wall_color)
        if self.has_right_wall:
            rw = Line(Point(pbr.x, ptl.y), Point(pbr.x, pbr.y))
            self.__win.draw_line(rw, self.wall_color)
        if self.has_top_wall:
            tw = Line(Point(ptl.x, ptl.y), Point(pbr.x, ptl.y))
            self.__win.draw_line(tw, self.wall_color)
        if self.has_bottom_wall:
            bw = Line(Point(ptl.x, pbr.y), Point(pbr.x, pbr.y))
            self.__win.draw_line(bw, self.wall_color)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        fcx = (self.__x2 - self.__x1) / 2 + self.__x1
        fcy = (self.__y2 - self.__y1) / 2 + self.__y1
        tcx = (to_cell.__x2 - to_cell.__x1) / 2 + to_cell.__x1
        tcy = (to_cell.__y2 - to_cell.__y1) / 2 + to_cell.__y1
        print(f"({fcx}, {fcy}) to ({tcx}, {tcy})")
        fcell = Point(fcx, fcy)
        tcell = Point(tcx, tcy)
        path = Line(fcell, tcell)
        self.__win.draw_line(path, line_color)


win = Window(800, 600)

c1 = Cell(win)
c1.has_right_wall = False
c1.draw(Point(50, 50), Point(100, 100))

c2 = Cell(win)
c2.has_left_wall = False
c2.has_bottom_wall = False
c2.draw(Point(100, 50), Point(150, 100))

c1.draw_move(c2)

c3 = Cell(win)
c3.has_top_wall = False
c3.has_right_wall = False
c3.draw(Point(100, 100), Point(150, 150))

c2.draw_move(c3)

c4 = Cell(win)
c4.has_left_wall = False
c4.draw(Point(150, 100), Point(200, 150))

c3.draw_move(c4, True)

win.wait_for_close()
