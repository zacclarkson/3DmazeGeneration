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
    TODO: Complete the implementation (Task A)
    """
	

    def generateMaze(self, maze:Maze3D):
        # Initialize cells and walls
        maze.initCells(addWallFlag=True)

        # Randomly select a starting cell
        start_level = random.randint(0, maze.levelNum() - 1)
        start_row = random.randint(0, maze.rowNum(start_level) - 1)
        start_col = random.randint(0, maze.colNum(start_level) - 1)
        start_cell = Coordinates3D(start_level, start_row, start_col)

        # Mark the start cell as visited and initialize the frontier list
        visited = set()
        frontier = []

        def add_frontier(cell):
            for neighbor in maze.neighbours(cell):
                if neighbor not in visited:
                    frontier.append((cell, neighbor))

        visited.add(start_cell)
        add_frontier(start_cell)

        while frontier:
            # Randomly select a wall from the frontier list
            cell, neighbor = random.choice(frontier)
            frontier.remove((cell, neighbor))

            if neighbor not in visited:
                # Remove the wall between cell and neighbor
                maze.removeWall(cell, neighbor)
                visited.add(neighbor)
                add_frontier(neighbor)

        # Add entrances and exits as needed
        self.add_entrances_and_exits(maze)

    def add_entrances_and_exits(self, maze: Maze3D):
        # Example to add a single entrance and exit, modify as needed
        entrance = Coordinates3D(0, 0, 0)
        exit = Coordinates3D(maze.levelNum() - 1, maze.rowNum(maze.levelNum() - 1) - 1, maze.colNum(maze.levelNum() - 1) - 1)
        
        maze.storeEntrance(entrance)
        maze.storeExit(exit)
        
        maze.carveEntrances()
        maze.carveExits()

        