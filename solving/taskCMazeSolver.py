# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Task C solver.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


from collections import deque
from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D

class TaskCMazeSolver(MazeSolver):
    """
    Task C solver implementation.  You'll need to complete its implementation for task C.
    """

    def __init__(self):
        super().__init__()
        self.m_name = "taskC"
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
        # we call the the solve maze call without the entrance.
        # DO NOT CHANGE THIS METHOD
        self.solveMazeTaskC(maze)

    def solveMazeTaskC(self, maze: Maze3D):
        """       
        solve the maze, used by Task C.
        This version of solveMaze does not provide a starting entrance, and as part of the solution, the method should
        to find the entrance and exit pair (see project specs for requirements of this task).
        TODO: Please complete this implementation for task C.  You should call maze.solved(...) to update which entrance
        and exit you used for task C.

        @param maze: Instance of maze to solve.
        """
        entrances = maze.getEntrances()
        num_exits = len(maze.getExits())
        
        all_paths = {}
        all_costs = {}

        for entrance in entrances:
            paths, costs = self.bfs_explore(maze, entrance, num_exits)
            all_paths[entrance] = paths
            all_costs[entrance] = costs

        best_pair, best_cost = self.find_best_pair(all_paths, all_costs)
        entrance, exit = best_pair
        path = all_paths[entrance][exit]

        self.solverPathAppend(path)
        maze.solved(entrance, exit)

    def bfs_explore(self, maze, start, num_exits):
        queue = deque([(start, 0, [start])])  # (cell, distance, path)
        visited = set()
        paths = {}
        costs = {}
        exits_found = 0

        while queue and exits_found < num_exits:
            current_cell, distance, path = queue.popleft()
            visited.add(current_cell)

            if current_cell in maze.getExits():
                paths[current_cell] = path
                costs[current_cell] = len(visited) + distance
                exits_found += 1

            for direction in self.directions:
                next_cell = self.get_next_cell(current_cell, direction)
                if self.can_move(maze, current_cell, next_cell) and next_cell not in visited:
                    queue.append((next_cell, distance + 1, path + [next_cell]))

        return paths, costs

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

    def find_best_pair(self, all_paths, all_costs):
        best_pair = None
        best_cost = float('inf')

        for entrance, costs in all_costs.items():
            for exit, cost in costs.items():
                if cost < best_cost:
                    best_cost = cost
                    best_pair = (entrance, exit)

        return best_pair, best_cost







    

