from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.winfo_width = width
        self.__root.winfo_height = height
        self.__canv = Canvas(self.__root)
        self.__canv.pack()
        active = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.active = True
        while self.active:
            self.redraw()
    
    def close(self):
        self.active = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canv, fill_color)

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    
    def __init__(self, one, two):
        self.one = one
        self.two = two
        
    def draw(self, canvas, fill_color):
        canvas.create_line(self.one.x, self.one.y, self.two.x, self.two.y, fill=fill_color, width=2)
        canvas.pack()

win = Window(800, 600)
p1 = Point(1, 1)
p2 = Point(1, 50)
line1 = Line(p1, p2)
win.draw_line(line1, fill_color="black")
win.wait_for_close()