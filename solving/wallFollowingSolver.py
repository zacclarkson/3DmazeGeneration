# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Wall following maze solver.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D
import random
from enum import Enum

class WallFollowingMazeSolver(MazeSolver):
    """
    Wall following solver implementation. You'll need to complete its implementation for task B.
    """

    class Direction(Enum):
        NORTH = 'N'
        UP = 'U'
        EAST = 'E'
        SOUTH = 'S'
        DOWN = 'D'
        WEST = 'W'

    def __init__(self):
        super().__init__()
        self.direction_vectors = {
            self.Direction.NORTH: (0, -1, 0),
            self.Direction.UP: (1, 0, 0),
            self.Direction.EAST: (0, 0, 1),
            self.Direction.SOUTH: (0, 1, 0),
            self.Direction.DOWN: (-1, 0, 0),
            self.Direction.WEST: (0, 0, -1)
        }

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        self.m_solverPath.append((self.m_entranceUsed, False))

        currentDirection = self.Direction.NORTH
        currentCell = entrance
        self.m_cellsExplored += 1
        nextCell = self.getNextCell(currentCell, currentDirection)

        while nextCell not in maze.getExits():
            print("Starting loop iteration")
            print("Current cell: ", currentCell, "Current direction: ", currentDirection)
            print("Next cell: ", nextCell)

            # Check if there's a right wall or if it's clear to move
            if self.checkRightWall(maze, currentCell, currentDirection):
                print("Right opening detected - turning right")
                currentDirection = self.turnRight(currentDirection)
            elif self.okToMove(maze, currentCell, nextCell):
                print("Path clear - moving forward")
                self.m_solverPath.append((nextCell, False))
                self.m_cellsExplored += 1
                currentCell = nextCell  # update current cell to next cell
            else:
                print("Wall detected - turning left")
                currentDirection = self.turnLeft(currentDirection)

            # After updating direction or moving, calculate the next cell for the new current state
            print("Preparing to calculate next cell based on new state")
            nextCell = self.getNextCell(currentCell, currentDirection)
            print("Next cell for upcoming loop iteration: ", nextCell)
            print("Repeating loop")

            print("End of loop iteration\n")
            
        
        self.m_solverPath.append((nextCell, False))
        self.m_cellsExplored += 1
        self.m_exitUsed = nextCell
        self.m_solved = True
        return

            

    def getNextCell(self, currentCell: Coordinates3D, currentDirection: Direction) -> Coordinates3D:
        print("getNextCell called")
        delta = self.direction_vectors[currentDirection]
        nextCell = Coordinates3D(currentCell.getLevel() + delta[0], currentCell.getRow() + delta[1], currentCell.getCol() + delta[2])
        print("Current cell in getNextCell: ", currentCell)
        print("Direction vector in getNextCell: ", delta)
        print("Next cell called returning: ", nextCell)
        return nextCell
    
    def checkRightWall(self, maze: Maze3D, currentCell: Coordinates3D, currentDirection: Direction) -> bool:
        print("checkRightWall called")
        # Get a list of all Direction enum members
        directions = list(self.Direction)
        # Find the index of the current direction
        current_index = directions.index(currentDirection)
        # Compute the index for the right direction (90 degrees clockwise)
        right_index = (current_index + 1) % len(directions)
        # Get the right direction using the new index
        rightDirection = directions[right_index]
        # Get the next cell to the right based on the right direction
        print("calling getNextCell with right direction: ", rightDirection)
        rightCell = self.getNextCell(currentCell, rightDirection)
        # Check if there's a wall between the current cell and the right cell
        print("Checking right wall from ", currentCell, " to ", rightCell)
        okToMove = self.okToMove(maze, currentCell, rightCell)
        print("rightCell ok to move: ", okToMove) 
        return okToMove
        
    def turnLeft(self, currentDirection):
        # Get a list of all Direction enum members
        directions = list(self.Direction)
        # Find the index of the current direction
        current_index = directions.index(currentDirection)
        # Calculate the new index for turning left (decrement and wrap around)
        left_index = (current_index - 1) % len(directions)
        # Get the new direction from the list using the left index
        newDirection = directions[left_index]
        print("Turning left from ", currentDirection, " to ", newDirection)
        return newDirection
    
    def turnRight(self, currentDirection):
        # Get a list of all Direction enum members
        directions = list(self.Direction)
        # Find the index of the current direction
        current_index = directions.index(currentDirection)
        # Calculate the new index for turning right (increment and wrap around)
        right_index = (current_index + 1) % len(directions)
        # Get the new direction from the list using the right index
        newDirection = directions[right_index]
        print("Turning right from ", currentDirection, " to ", newDirection)
        return newDirection
    
    def okToMove(self, maze: Maze3D, currentCell: Coordinates3D, nextCell: Coordinates3D) -> bool:
        return maze.checkCoordinates(nextCell) and not maze.hasWall(currentCell, nextCell) and not maze.isBoundary(nextCell)
