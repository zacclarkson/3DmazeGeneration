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

class WallFollowingMazeSolver(MazeSolver):
    """
    Wall following solver implementation. You'll need to complete its implementation for task B.
    """
    def __init__(self):
        super().__init__()
        self.m_name = "wallFollowing"
        self.directions = ['N', 'E', 'S', 'W', 'U', 'D']  # Possible directions
        self.direction_vectors = {
            'N': (0, -1, 0),
            'S': (0, 1, 0),
            'E': (0, 0, 1),
            'W': (0, 0, -1),
            'U': (1, 0, 0),
            'D': (-1, 0, 0)
        }

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        current_cell = entrance
        current_direction = 'E'  # Start by facing East
        visited = set([current_cell])
        self.solverPathAppend(current_cell, False)
        
        while current_cell not in maze.getExits():
            right_direction = self.get_right_direction(current_direction)
            forward_cell = self.get_next_cell(current_cell, current_direction)
            right_cell = self.get_next_cell(current_cell, right_direction)
            
            if self.can_move(maze, current_cell, right_cell):
                current_direction = right_direction
                current_cell = right_cell
            elif self.can_move(maze, current_cell, forward_cell):
                current_cell = forward_cell
            else:
                current_direction = self.get_left_direction(current_direction)
            
            visited.add(current_cell)
            self.solverPathAppend(current_cell, False)

        if current_cell in maze.getExits():
            self.solved(entrance, current_cell)

    def get_right_direction(self, current_direction):
        direction_order = ['N', 'E', 'S', 'W', 'U', 'D']
        idx = direction_order.index(current_direction)
        return direction_order[(idx + 1) % 6]

    def get_left_direction(self, current_direction):
        direction_order = ['N', 'E', 'S', 'W', 'U', 'D']
        idx = direction_order.index(current_direction)
        return direction_order[(idx - 1) % 6]

    def get_next_cell(self, current_cell, direction):
        level, row, col = current_cell.getLevel(), current_cell.getRow(), current_cell.getCol()
        dlevel, drow, dcol = self.direction_vectors[direction]
        return Coordinates3D(level + dlevel, row + drow, col + dcol)

    def can_move(self, maze, from_cell, to_cell):
        if not maze.checkCoordinates(to_cell):
            return False
        if maze.hasWall(from_cell, to_cell):
            return False
        return True
