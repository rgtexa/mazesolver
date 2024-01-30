from graphics import Window, Point
from maze import Maze


def main():
    rows = 12
    cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / cols
    cell_size_y = (screen_y - 2 * margin) / rows

    win = Window(screen_x, screen_y)

    maze = Maze(Point(margin, margin), rows, cols, cell_size_x, cell_size_y, win, 10)
    maze.solve()

    win.wait_for_close()


main()
