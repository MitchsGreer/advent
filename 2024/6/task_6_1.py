"""
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

    If there is something directly in front of you, turn right 90 degrees.
    Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..

In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Union


@dataclass
class Coordinate:
    row: int
    column: int


__INPUT_FILE = Path(Path(__file__).parent, "task_6_1.txt")


def from_txt(input_file: Union[Path, str]) -> List[List[str]]:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    grid: List[List[str]] = []
    with open(input_file, "r") as in_file:
        for line in in_file.readlines():
            grid.append(list(line.strip()))

    return grid


def _find_start(grid: List[List[str]]) -> Coordinate:
    """Find the starting place of the guard in the grid.

    Args:
        grid: The grid to search.

    Returns:
        The coordinates for the starting place.
    """
    start_row = 0
    start_column = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "^":
                start_row = row
                start_column = column

                break

    return Coordinate(start_row, start_column)


def _move_down(
    grid: List[List[str]], coords: Coordinate
) -> Tuple[bool, int, Coordinate]:
    """Move down through the grid until we hit an obstacle or go off of the grid.

    Args:
        grid: The grid to move through.
        coords: The starting coordinates.

    Returns:
        A flag for the guard remaining in the grid, the number of spaces visited, and the ending coordinates of the guard.
    """
    hit_obstacle = False
    ending_coords = coords
    cells_visited = 0
    for row in range(coords.row, len(grid), 1):

        # Obstruction hit! Stop moving and return previous coordinates.
        if grid[row][coords.column] == "#":
            hit_obstacle = True
            ending_coords = Coordinate(row - 1, coords.column)
            break

        elif grid[row][coords.column] != "V":
            grid[row][coords.column] = "V"
            cells_visited += 1

    return hit_obstacle, cells_visited, ending_coords


def _move_right(
    grid: List[List[str]], coords: Coordinate
) -> Tuple[bool, int, Coordinate]:
    """Move right through the grid until we hit an obstacle or go off of the grid.

    Args:
        grid: The grid to move through.
        coords: The starting coordinates.

    Returns:
        A flag for the guard remaining in the grid, the number of spaces visited, and the ending coordinates of the guard.
    """
    hit_obstacle = False
    ending_coords = coords
    cells_visited = 0
    for column in range(coords.column, len(grid[0]), 1):

        # Obstruction hit! Stop moving and return previous coordinates.
        if grid[coords.row][column] == "#":
            hit_obstacle = True
            ending_coords = Coordinate(coords.row, column - 1)
            break

        elif grid[coords.row][column] != "V":
            grid[coords.row][column] = "V"
            cells_visited += 1

    return hit_obstacle, cells_visited, ending_coords


def _move_up(grid: List[List[str]], coords: Coordinate) -> Tuple[bool, int, Coordinate]:
    """Move up through the grid until we hit an obstacle or go off of the grid.

    Args:
        grid: The grid to move through.
        coords: The starting coordinates.

    Returns:
        A flag for the guard remaining in the grid, the number of spaces visited, and the ending coordinates of the guard.
    """
    hit_obstacle = False
    ending_coords = coords
    cells_visited = 0
    for row in range(coords.row, -1, -1):

        # Obstruction hit! Stop moving and return previous coordinates.
        if grid[row][coords.column] == "#":
            hit_obstacle = True
            ending_coords = Coordinate(row + 1, coords.column)
            break

        elif grid[row][coords.column] != "V":
            grid[row][coords.column] = "V"
            cells_visited += 1

    return hit_obstacle, cells_visited, ending_coords


def _move_left(
    grid: List[List[str]], coords: Coordinate
) -> Tuple[bool, int, Coordinate]:
    """Move left through the grid until we hit an obstacle or go off of the grid.

    Args:
        grid: The grid to move through.
        coords: The starting coordinates.

    Returns:
        A flag for the guard remaining in the grid, the number of spaces visited, and the ending coordinates of the guard.
    """
    hit_obstacle = False
    ending_coords = coords
    cells_visited = 0
    for column in range(coords.column, -1, -1):

        # Obstruction hit! Stop moving and return previous coordinates.
        if grid[coords.row][column] == "#":
            hit_obstacle = True
            ending_coords = Coordinate(coords.row, column + 1)
            break

        elif grid[coords.row][column] != "V":
            grid[coords.row][column] = "V"
            cells_visited += 1

    return hit_obstacle, cells_visited, ending_coords


def _travel(grid: List[List[str]], starting_coords: Coordinate) -> int:
    """Travel the guard through the grid until the leave it.

    Args:
        starting_coords: The starting x and y positions.
        grid: The grid to travel through.

    Returns:
        The number of squares, including the first one, the guard visited.
    """
    visited_cells = 0

    guard_in_grid = True
    current_coordinates = starting_coords
    while guard_in_grid:

        for move in [_move_up, _move_right, _move_down, _move_left]:

            if not guard_in_grid:
                break

            guard_in_grid, spaces_visited, current_coordinates = move(
                grid, current_coordinates
            )
            visited_cells += spaces_visited

    return visited_cells


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    grid = from_txt(__INPUT_FILE)

    return _travel(grid, _find_start(grid))


if __name__ == "__main__":
    print(task())
