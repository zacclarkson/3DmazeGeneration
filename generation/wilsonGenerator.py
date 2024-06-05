# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Wilson's algorithm maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

import random
from typing import List
from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator


class WilsonMazeGenerator(MazeGenerator):
    """
    Wilson algorithm maze generator.
    """
	

    def generateMaze(self, maze: Maze3D):
        # Initialize cells and add walls between adjacent cells
        maze.initCells(addWallFlag=True)

        unfinishedCells = list(maze.allCells())
        

        startLevel = random.randint(0, maze.levelNum() - 1)
        startRow = random.randint(0, maze.colNum(startLevel) - 1)
        startCol = random.randint(0, maze.colNum(startLevel) - 1)
        startCoord = Coordinates3D(startLevel, startRow, startCol)

        finishedCells = set()
        finishedCells.add(startCoord)


        while unfinishedCells:
            # randomly select a cell from unfinishedCells
            selectedCell = random.choice(unfinishedCells)
            # perform random walk until destinationCell is reached
            path = self.walk(maze, selectedCell, finishedCells)

            # carve path and add to finishedCells
            for i in range(len(path) - 1):
                curCell = path[i]
                if i + 1 < len(path):  # Check if nextCell index is valid
                    nextCell = path[i + 1]
                    maze.removeWall(curCell, nextCell)
                    finishedCells.append(curCell)
        
        self.m_mazeGenerated = True

    


    def walk(self, maze: Maze3D, startCoord: Coordinates3D, finishedCells: set) -> List[Coordinates3D]:
        curCell = startCoord
        path = [curCell]

        while curCell not in finishedCells:
            unvisitedNeighbors = [
                neighbor
                for neighbor in maze.neighbours(curCell)
                if maze.checkCoordinates(neighbor) and not maze.isBoundary(neighbor) and neighbor not in path and neighbor not in finishedCells
            ]

            if unvisitedNeighbors:
                nextCell = random.choice(unvisitedNeighbors)
                curCell = nextCell
                path.append(curCell)
            else:
                if path: 
                    curCell = path.pop()
                else:
                    # If the path is empty AND curCell is still not finalized, there's no solution.
                    return None  # Return None to signal an invalid walk
        return path


        
        

    
		
        
        
		