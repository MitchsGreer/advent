"""
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

from pathlib import Path
from typing import List, Union

__INPUT_FILE = Path(Path(__file__).parent, "task_4_2.txt")


def from_txt(input_file: Union[Path, str]) -> List[List[str]]:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    letter_grid = []
    with open(input_file, "r") as in_file:
        for line in in_file.readlines():
            letter_grid.append(list(line.strip()))

    return letter_grid


def _check_string(line: str, keyword: str) -> bool:
    """Search the given line for `XMAS` or `SAMX`.

    Args:
        line: Check the line string for the given keyword.
        keyword: The keyword to check for.

    Returns:
        True if the keyword or reverse is in the line, False otherwise.
    """
    in_string = False
    if keyword in line or keyword[::-1] in line:
        in_string = True

    return in_string


def _check_small_grid(grid: List[List[str]]) -> int:
    """Check the small grid in an X pattern and the top of the grid.

    Args:
        grid: The grid to check.

    Returns:
        The number of substrings found.
    """
    substring_finds = 0

    # Diagonal check `\`.
    if len(grid) == len(grid[0]):
        line = ""
        for x in range(len(grid)):
            line += grid[x][x]

        if _check_string(line, "MAS"):
            substring_finds += 1

    # Diagonal check `/`.
    if len(grid) == len(grid[0]):
        line = ""
        for x in range(len(grid)):
            line += grid[x][-(x + 1)]

        if _check_string(line, "MAS"):
            substring_finds += 1

    if substring_finds == 2:
        substring_finds = 1
    else:
        substring_finds = 0

    return substring_finds


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    letter_grid = from_txt(__INPUT_FILE)
    substring_finds = 0

    for x in range(len(letter_grid)):
        for y in range(len(letter_grid[0])):

            small_grid = letter_grid[x : min(x + 3, len(letter_grid))]
            for z in range(len(small_grid)):
                small_grid[z] = small_grid[z][y : min(y + 3, len(letter_grid))]

            substring_finds += _check_small_grid(small_grid)

    return substring_finds


if __name__ == "__main__":
    print(task())
