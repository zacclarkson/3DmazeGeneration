# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Wilson's algorithm maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

import random
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

        # Directions for movement: N, S, E, W, U, D (Up, Down for 3D)
        DIRECTIONS = {
            'N': (-1, 0, 0),
            'S': (1, 0, 0),
            'E': (0, 1, 0),
            'W': (0, -1, 0),
            'U': (0, 0, 1),
            'D': (0, 0, -1)
        }
        OPPOSITE = {
            'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E', 'U': 'D', 'D': 'U'
        }

        # Select a random starting cell
        start_level = random.randint(0, maze.levelNum() - 1)
        start_row = random.randint(0, maze.rowNum(start_level) - 1)
        start_col = random.randint(0, maze.colNum(start_level) - 1)
        start_cell = Coordinates3D(start_level, start_row, start_col)
        maze.addVertex(start_cell)

        # Mark the starting cell as part of the maze
        in_maze = {start_cell}

        # Function to check if a coordinate is within bounds
        def in_bounds(cell):
            l, r, c = cell.getLevel(), cell.getRow(), cell.getCol()
            return (0 <= l < maze.levelNum() and
                    0 <= r < maze.rowNum(l) and
                    0 <= c < maze.colNum(l))

        # Random walk to find a path from an unvisited cell to the maze
        while len(in_maze) < maze.cellNum(0) * maze.levelNum():
            current_level = random.randint(0, maze.levelNum() - 1)
            current_row = random.randint(0, maze.rowNum(current_level) - 1)
            current_col = random.randint(0, maze.colNum(current_level) - 1)
            current_cell = Coordinates3D(current_level, current_row, current_col)

            if current_cell in in_maze:
                continue

            path = [current_cell]
            visited = {current_cell: None}

            while current_cell not in in_maze:
                direction = random.choice(list(DIRECTIONS.keys()))
                next_level = current_cell.getLevel() + DIRECTIONS[direction][0]
                next_row = current_cell.getRow() + DIRECTIONS[direction][1]
                next_col = current_cell.getCol() + DIRECTIONS[direction][2]
                next_cell = Coordinates3D(next_level, next_row, next_col)

                if in_bounds(next_cell):
                    if next_cell in visited:
                        cycle_start = path.index(next_cell)
                        path = path[:cycle_start + 1]
                    else:
                        path.append(next_cell)
                        visited[next_cell] = direction
                    current_cell = next_cell

            # Carve the path into the maze
            for cell in path:
                in_maze.add(cell)
                if visited[cell]:
                    direction = visited[cell]
                    prev_cell = Coordinates3D(
                        cell.getLevel() - DIRECTIONS[direction][0],
                        cell.getRow() - DIRECTIONS[direction][1],
                        cell.getCol() - DIRECTIONS[direction][2]
                    )
                    maze.removeWall(prev_cell, cell)
                    in_maze.add(cell)

    
		
        
        
		