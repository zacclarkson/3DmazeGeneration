# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Implementation of Task D maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator
import random

class TaskDMazeGenerator(MazeGenerator):
    """
    Task D maze generator implementation. You'll need to complete its implementation for task D.
    """
    def __init__(self):
        super().__init__()
        self.m_name = "taskD"

    def generateMaze(self, maze: Maze3D, solver):
        # Query the solver for its name
        solver_name = solver.getName()
        
        if solver_name == "wallFollowing":
            self.generateWallFollowingMaze(maze)
        elif solver_name == "pledge":
            self.generatePledgeMaze(maze)
        else:
            self.generateGeneralMaze(maze)

    def generateWallFollowingMaze(self, maze: Maze3D):
        """
        Generate a maze that is challenging for wall-following solvers.
        """
        maze.initCells(addWallFlag=True)
        
        # Create a pattern of long corridors with many dead ends
        levels = maze.levelNum()
        for level in range(levels):
            rows = maze.rowNum(level)
            cols = maze.colNum(level)
            for row in range(rows):
                for col in range(0, cols - 1, 2):
                    if col + 2 < cols:
                        maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row, col + 2))
                    if row + 1 < rows:
                        maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row + 1, col))

    def generatePledgeMaze(self, maze: Maze3D):
        """
        Generate a maze that is challenging for pledge solvers.
        """
        maze.initCells(addWallFlag=True)
        
        # Create loops and multiple paths
        levels = maze.levelNum()
        for level in range(levels):
            rows = maze.rowNum(level)
            cols = maze.colNum(level)
            for row in range(0, rows - 1, 2):
                for col in range(0, cols - 1, 2):
                    if row + 2 < rows:
                        maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row + 2, col))
                    if col + 2 < cols:
                        maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row, col + 2))
                    if row + 1 < rows and col + 1 < cols:
                        maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row + 1, col + 1))

    def generateGeneralMaze(self, maze: Maze3D):
        """
        Generate a general challenging maze for any solver.
        """
        maze.initCells(addWallFlag=True)
        
        # Create a combination of dead ends, loops, and multiple paths
        levels = maze.levelNum()
        for level in range(levels):
            rows = maze.rowNum(level)
            cols = maze.colNum(level)
            for row in range(rows):
                for col in range(cols):
                    if random.random() > 0.5:
                        if col + 1 < cols:
                            maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row, col + 1))
                        if row + 1 < rows:
                            maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row + 1, col))
                    if random.random() > 0.7:
                        if col + 1 < cols and row + 1 < rows:
                            maze.removeWall(Coordinates3D(level, row, col), Coordinates3D(level, row + 1, col + 1))	