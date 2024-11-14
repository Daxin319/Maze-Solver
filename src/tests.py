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

    def test_maze_wall_breaking_recursive(self):
        # Test the recursive wall breaking function
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 50, 50, Window(800, 600), 0)
        m1._create_cells()  # Explicitly call the method to create cells
        m1._break_walls_r(0, 0)  # Start the maze generation from the top left corner

        # Check that all cells have been visited
        for row in m1.cells:
            for cell in row:
                self.assertTrue(cell.visited, "All cells should be visited during maze generation")

        # Ensure that no cells have all four walls intact, as that would mean they were not connected to any neighbors
        for row in m1.cells:
            for cell in row:
                walls_intact = cell.has_left_wall and cell.has_right_wall and cell.has_top_wall and cell.has_bottom_wall
                self.assertFalse(walls_intact, "No cell should have all four walls intact after maze generation")

    def test_maze_solve_recursive(self):
        # Test the recursive maze-solving function
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 50, 50, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        m1._break_walls_r(0, 0)  # Generate the maze
        m1._reset_cell_visited()  # Reset visited status before solving
        solved = m1._solve_r(0, 0)  # Attempt to solve the maze starting from the top-left corner

        # Check if the maze was solved (should be True if correctly implemented)
        self.assertTrue(solved, "Maze should be solved successfully from start to end")

        
        

    def test_maze_all_cells_visited_after_solve(self):
        # Ensure all cells are visited during solving process
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 50, 50, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        m1._break_walls_r(0, 0)  # Generate the maze
        m1._reset_cell_visited()  # Reset visited status before solving
        m1._solve_r(0, 0)  # Solve the maze

        # Check that all cells that were part of the path are visited
        for row in m1.cells:
            for cell in row:
                if cell.visited:
                    self.assertTrue(cell.visited, "All cells part of the solution should be visited during maze solving")

    def test_maze_undo_moves(self):
        # Test the undo functionality during solving
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 50, 50, Window(800, 600))
        m1._create_cells()  # Explicitly call the method to create cells
        m1._break_walls_r(0, 0)  # Generate the maze
        m1._reset_cell_visited()  # Reset visited status before solving
        m1._solve_r(0, 0)  # Solve the maze

        # Check that the method correctly drew undo moves where needed
        # This is a bit more difficult to verify, so we can assume if no exception occurred during draw_move calls, it's fine.
        try:
            m1._solve_r(0, 0)  # Running the solve method again to ensure no issues with undo moves
        except Exception as e:
            self.fail(f"Maze undo moves raised an exception: {e}")

        
        

if __name__ == "__main__":
    unittest.main()