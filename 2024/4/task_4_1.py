"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?
"""

from pathlib import Path
from typing import List, Union

__INPUT_FILE = Path(Path(__file__).parent, "task_4_1.txt")


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

    # Horizontal check.
    if _check_string("".join([el[0] for el in grid]), "XMAS"):
        substring_finds += 1

    # Vertical check.
    if _check_string("".join(grid[0]), "XMAS"):
        substring_finds += 1

    # Diagonal check `\`.
    if len(grid) == len(grid[0]):
        line = ""
        for x in range(len(grid)):
            line += grid[x][x]

        if _check_string(line, "XMAS"):
            substring_finds += 1

    # Diagonal check `/`.
    if len(grid) == len(grid[0]):
        line = ""
        for x in range(len(grid)):
            line += grid[x][-(x + 1)]

        if _check_string(line, "XMAS"):
            substring_finds += 1

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

            small_grid = letter_grid[x : min(x + 4, len(letter_grid))]
            for z in range(len(small_grid)):
                small_grid[z] = small_grid[z][y : min(y + 4, len(letter_grid))]

            substring_finds += _check_small_grid(small_grid)

    return substring_finds


if __name__ == "__main__":
    print(task())
