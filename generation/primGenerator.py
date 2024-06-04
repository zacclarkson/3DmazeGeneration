# -------------------------------------------------------------------
# Prim's maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

import random
from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator



class PrimMazeGenerator(MazeGenerator):
    """
    Prim's algorithm maze generator.  
    """
    def generateMaze(self, maze: Maze3D):
        # Initialize cells and add walls between adjacent cells
        maze.initCells(addWallFlag=True)

        # Choose a random starting cell
        start_level = random.randint(0, maze.levelNum() - 1)
        start_row = random.randint(0, maze.rowNum(start_level) - 1)
        start_col = random.randint(0, maze.colNum(start_level) - 1)
        start_cell = Coordinates3D(start_level, start_row, start_col)
        
        # Mark the starting cell as part of the maze
        selected = set()
        selected.add(start_cell)

        # Priority queue (or list) of walls adjacent to the cells in the maze
        walls = maze.neighbourWalls(start_cell)
        random.shuffle(walls)  # Shuffle for randomness

        while walls:
            wall = walls.pop()
            cell1 = wall.cell1
            cell2 = wall.cell2

            # Check if exactly one of the cells on either side of the wall is in the maze
            if (cell1 in selected) ^ (cell2 in selected):
                # Remove the wall to carve a path in the maze
                maze.removeWall(cell1, cell2)

                # Add the new cell to the maze
                new_cell = cell1 if cell2 in selected else cell2
                selected.add(new_cell)

                # Add the walls of the new cell to the list
                new_walls = maze.neighbourWalls(new_cell)
                random.shuffle(new_walls)
                walls.extend(new_walls)

        