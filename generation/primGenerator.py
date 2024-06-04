# -------------------------------------------------------------------
# Prim's maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

import random
from typing import List
from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator


class PrimMazeGenerator(MazeGenerator):
    """
    Prim's algorithm maze generator.  
    """

    def generateMaze(self, maze: Maze3D):
        # Initialize cells and add walls between adjacent cells
        maze.initCells(True)

        # Get the list of entrances
        mazeEntrances = maze.getEntrances()

        # Choose a random entrance as the starting cell
        startCell = random.choice(mazeEntrances)
        visitedCells = [startCell]
        
        currCell = startCell

# Note: The frontier now stores Coordinates3D (cells)
        frontier = maze.neighbours(currCell)

        while frontier:
            selectedCell = random.choice(frontier)

            # Find unvisited neighbors of the selected cell, excluding boundary cells
            unvisitedNeighbors = [neighbor for neighbor in maze.neighbours(selectedCell)
                                if neighbor not in visitedCells and not maze.isBoundary(neighbor)]

            if unvisitedNeighbors:
                # Choose a random unvisited neighbor
                visitedNeighbor = random.choice(unvisitedNeighbors)

                # Remove the wall between the selected cell and its neighbor
                maze.removeWall(selectedCell, visitedNeighbor)

                # Update sets and frontier
                visitedCells.append(selectedCell)
                frontier.remove(selectedCell)
                frontier.extend(unvisitedNeighbors)  

            else:
                # If no unvisited neighbors, remove the cell from the frontier
                frontier.remove(selectedCell)
        
        # Set maze generated flag to True when done
        self.m_mazeGenerated = True
