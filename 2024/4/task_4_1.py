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

import re
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


def search_lines(line: List[str]) -> int:
    """Search the given line for `XMAS` or `SAMX`.

    Args:
        line: The line to search.

    Returns:
        The number of times the substring appear in the given string.
    """
    substrings_found = 0
    substrings_found += len(re.findall("XMAS", "".join(line)))
    substrings_found += len(re.findall("SAMX", "".join(line)))

    return substrings_found


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    letter_grid = from_txt(__INPUT_FILE)
    substring_finds = 0

    # search horizontal lines.
    for row in letter_grid:
        substring_finds += search_lines(row)

    # Search vertical lines.
    for column_number in range(len(letter_grid[0])):
        line = [letter_grid[x][column_number] for x in range(len(letter_grid))]
        substring_finds += search_lines(line)

    # Search diagonal lines `/` this way.
    for num in range(0, (len(letter_grid) + len(letter_grid[0])) // 2):
        line = []
        x = 0

        row_length = len(letter_grid[x])
        column_length = len(letter_grid[x][0])

        wrap_count = 0
        for x in range(num // 3, num + column_length, 1):
            for y in range(min(num, column_length), -1, -1):
                line.append(letter_grid[x % column_length][y])

            wrap_count = x // column_length

        print(line)
    #     substring_finds += search_lines(line)

    # # Search diagonal lines `/` this way, this is the second half, excluding the main diagonal.
    # for num in range(1, ((len(letter_grid) + len(letter_grid[0])) // 2)):
    #     line = []
    #     x = 1
    #     for y in range(num, 0, -1):
    #         line.append(letter_grid[-x][-y])
    #         x += 1

    #     print(line)
    #     substring_finds += search_lines(line)

    # # Search diagonal lines `\` this way, this is the first half, including the biggest diagonal.
    # for num in range(1, (len(letter_grid) + len(letter_grid[0])) // 2):
    #     line = []
    #     y = 0
    #     for x in range(num, -1, -1):
    #         line.append(letter_grid[x][y])
    #         y += 1

    #     print(line)
    #     substring_finds += search_lines(line)

    # # Search diagonal lines `\` this way, this is the second half, excluding the main diagonal.
    # for num in range(1, ((len(letter_grid) + len(letter_grid[0])) // 2)):
    #     line = []
    #     y = 1
    #     for x in range(num, 0, -1):
    #         line.append(letter_grid[-x][-y])
    #         y += 1

    #     print(line)
    #     substring_finds += search_lines(line)

    return substring_finds

if __name__ == "__main__":
    print(task())
