"""
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

    156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
    192: 17 8 14 can be made true using 17 || 8 + 14.

Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Union


@dataclass
class Problem:
    solution: int
    nums: List[int]


__INPUT_FILE = Path(Path(__file__).parent, "task_7_2.txt")


def from_txt(input_file: Union[Path, str]) -> List[Problem]:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    problems = []
    with open(input_file) as in_file:
        for line in in_file.readlines():
            solution = int(line.split(":")[0])
            nums = list(map(int, line.split(":")[1].strip().split(" ")))

            problems.append(Problem(solution, nums))

    return problems


def ternary(num: int) -> str:
    """Return the string representation of the given number.

    Args:
        n: The number to convert.

    Returns:
        The base 3 representation of the given string.
    """
    if num == 0:
        return "0"
    nums = []
    while num:
        num, remainder = divmod(num, 3)
        nums.append(str(remainder))

    return "".join(reversed(nums))


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """

    # The current bug is that eval follows pemdas, we need to go left to right. Not pemdas.
    problem_data = from_txt(__INPUT_FILE)

    total_solutions = 0
    for problem in problem_data:
        num_operators = 3 ** (len(problem.nums) - 1)

        for op_rep in range(num_operators):
            bin_op_rep = ternary(op_rep).rjust(len(ternary(num_operators)) - 1, "0")

            value = problem.nums[0]
            for index, num in enumerate(problem.nums[1:]):
                if bin_op_rep[index] == "0":
                    value = int(str(value) + str(num))
                elif bin_op_rep[index] == "1":
                    value += num
                elif bin_op_rep[index] == "2":
                    value *= num

            if value == problem.solution:
                total_solutions += problem.solution
                break

    return total_solutions


if __name__ == "__main__":
    print(task())
