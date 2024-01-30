import unittest
from maze import Maze
from graphics import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        m1 = Maze(Point(0, 0), rows, cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            rows,
        )

    def test_maze_break_entrance_and_exit(self):
        cols = 12
        rows = 10
        m1 = Maze(Point(0, 0), rows, cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[cols - 1][rows - 1].has_bottom_wall,
            False,
        )

    def test_cell_visit_rest(self):
        cols = 12
        rows = 10
        m1 = Maze(Point(0, 0), rows, cols, 10, 10)
        for column in m1._cells:
            for cell in column:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
