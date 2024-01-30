from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, ptl, pbr):
        if self._win is None:
            return
        self._x1 = ptl.x
        self._y1 = ptl.y
        self._x2 = pbr.x
        self._y2 = pbr.y
        lw = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        tw = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        rw = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        bw = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall:
            self._win.draw_line(lw)
        else:
            self._win.draw_line(lw, "white")
        if self.has_top_wall:
            self._win.draw_line(tw)
        else:
            self._win.draw_line(tw, "white")
        if self.has_right_wall:
            self._win.draw_line(rw)
        else:
            self._win.draw_line(rw, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bw)
        else:
            self._win.draw_line(bw, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)
