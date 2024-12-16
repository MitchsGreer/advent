"""
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...

Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...

Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...

Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Union


@dataclass
class Coordinate:
    row: int
    column: int


__INPUT_FILE = Path(Path(__file__).parent, "task_6_2.txt")


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
    guard_in_grid = True
    current_coordinates = starting_coords
    start_coords = []
    loop = False
    while guard_in_grid and not loop:

        for move_type, move in enumerate(
            [_move_up, _move_right, _move_down, _move_left]
        ):

            if not guard_in_grid:
                break

            start_coords.append((current_coordinates, move_type))

            guard_in_grid, _, current_coordinates = move(grid, current_coordinates)

            # We are in a loop! We win!
            if (current_coordinates, (move_type + 1) % 4) in start_coords:
                loop = True

    return loop


def _get_empty_cells(grid: List[List[str]]) -> List[Coordinate]:
    """Get all of the empty cells in the grid.

    Args:
        grid: The grid to search trough.

    Returns:
        A list of empty cell coordinates.
    """
    empty_cells = []
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            if grid[row_index][column_index] == ".":
                empty_cells.append(Coordinate(row_index, column_index))

    return empty_cells


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    grid = from_txt(__INPUT_FILE)

    start = _find_start(grid)
    empty_cells = _get_empty_cells(grid)

    added_loops = 0
    for empty_cell in empty_cells:
        grid[empty_cell.row][empty_cell.column] = "#"
        loop = _travel(grid, start)
        grid[empty_cell.row][empty_cell.column] = "."

        if loop:
            added_loops += 1

    return added_loops


if __name__ == "__main__":
    print(task())
