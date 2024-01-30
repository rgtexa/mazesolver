from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title = "Maze Solver"
        self._canv = Canvas(self._root, bg="white", height=height, width=width)
        self._canv.pack(fill=BOTH, expand=1)
        self._active = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._active = True
        while self._active:
            self.redraw()

    def close(self):
        self._active = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canv, fill_color)


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
