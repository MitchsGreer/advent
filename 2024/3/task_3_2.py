"""
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

import re
from pathlib import Path
from typing import Union

__INPUT_FILE = Path(Path(__file__).parent, "task_3_2.txt")


def from_txt(input_file: Union[Path, str]) -> str:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    return Path(input_file).read_text()


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    input_str = from_txt(__INPUT_FILE)

    matches = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", input_str)
    num_of_products = 0
    multiplication_act = True
    for match in matches:
        match = [m for m in match if m][0]

        if match == "do()":
            multiplication_act = True

        if match == "don't()":
            multiplication_act = False

        if multiplication_act and re.match(r"(mul\(\d+,\d+\))", match) is not None:
            parsed = re.match(r"(?:mul)\((\d+),(\d+)\)", match)

            num_1 = parsed.group(1)
            num_2 = parsed.group(2)

            num_of_products += int(num_1) * int(num_2)

    return num_of_products


if __name__ == "__main__":
    print(task())
