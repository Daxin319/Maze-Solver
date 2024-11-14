import unittest

from maze import *


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        # Test creating a maze with cells
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_all_walls_present_initially(self):
        # Test if all walls are present initially for every cell
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        for row in m1.cells:
            for cell in row:
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)

    def test_maze_draw(self):
        # Test if the maze can be drawn without errors
        m1 = Maze(10, 10, 10, 10, 20, 20, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        try:
            for row in m1.cells:
                for cell in row:
                    cell.draw()
        except Exception as e:
            self.fail(f"Maze draw method raised an exception: {e}")

    def test_maze_path_drawing(self):
        # Test drawing paths between cells
        win = Window(800, 600)
        m1 = Maze(10, 10, 5, 5, 50, 50, win)
        m1._create_cells()  # Explicitly call the method to create cells
        cell_start = m1.cells[0][0]
        cell_end = m1.cells[0][1]
        try:
            cell_start.draw_move(cell_end)
        except Exception as e:
            self.fail(f"Maze path drawing raised an exception: {e}")

    def test_maze_undo_path(self):
        # Test undoing a drawn path between cells
        win = Window(800, 600)
        m1 = Maze(10, 10, 5, 5, 50, 50, win)
        m1._create_cells()  # Explicitly call the method to create cells
        cell_start = m1.cells[0][0]
        cell_end = m1.cells[0][1]
        try:
            cell_start.draw_move(cell_end, undo=False)  # Draw the path
            cell_start.draw_move(cell_end, undo=True)   # Undo the path
        except Exception as e:
            self.fail(f"Maze undo path raised an exception: {e}")

    def test_maze_entrance_and_exit_break(self):
        # Test if the entrance and exit are properly broken
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        m1._break_entrance_and_exit()  # Break entrance and exit

        # Check if the start cell has either top or left wall broken
        start_cell = m1.cells[0][0]
        broken_start_walls = int(not start_cell.has_left_wall) + int(not start_cell.has_top_wall)
        self.assertEqual(broken_start_walls, 1, "Start cell should have exactly one wall broken")

        # Check if the end cell has either bottom or right wall broken
        end_cell = m1.cells[-1][-1]
        broken_end_walls = int(not end_cell.has_right_wall) + int(not end_cell.has_bottom_wall)
        self.assertEqual(broken_end_walls, 1, "End cell should have exactly one wall broken")

if __name__ == "__main__":
    unittest.main()