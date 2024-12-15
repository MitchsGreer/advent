"""
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

from copy import deepcopy
from pathlib import Path
from typing import List, Union

__INPUT_FILE = Path(Path(__file__).parent, "task_2_2.txt")


def from_txt(input_file: Union[Path, str]) -> List[List[int]]:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    reports: List[List[int]] = []

    with open(input_file, "r") as input_fd:
        for line in input_fd.readlines():
            reports.append(list(map(lambda x: int(x), line.split())))

    return reports


def _check_nums(num_1: int, num_2: int) -> bool:
    """Check the given numbers to see if they are safe.

    The numbers are safe if:
        - They differ by at least one and at most three.

    Args:
        num_1: The first number.
        num_2: The second number.

    Returns:
        True if the numbers are safe, false otherwise.
    """
    distance = abs(num_1 - num_2)

    safe = True
    if distance == 0:
        safe = False

    if distance > 3:
        safe = False

    return safe


def _check_report(report: List[int], dampened: bool = False) -> bool:
    """Check the given report for safeness.

    Args:
        report: The report to check.

    Returns:
        True if the report is safe, false otherwise.
    """
    bad_report = False
    prev_distance = None
    for x in range(0, len(report) - 1, 1):
        distance = report[x] - report[x + 1]

        if not _check_nums(report[x], report[x + 1]) and not dampened:
            no_x = deepcopy(report)
            no_x.pop(x)

            no_x_1 = deepcopy(report)
            no_x_1.pop(x + 1)

            no_x = _check_report(no_x, dampened=True)
            no_x_1 = _check_report(no_x_1, dampened=True)
            if no_x and no_x_1:
                bad_report = True

            break

        elif not _check_nums(report[x], report[x + 1]):
            bad_report = True
            break

        elif prev_distance is not None and (
            (prev_distance > 0 and distance < 0) or (prev_distance < 0 and distance > 0)
        ):

            if not dampened:
                if x == 0:
                    no_x = deepcopy(report)
                    no_x.pop(x)

                    no_x_1 = deepcopy(report)
                    no_x_1.pop(x + 1)

                    no_x = _check_report(no_x, dampened=True)
                    no_x_1 = _check_report(no_x_1, dampened=True)
                    if no_x and no_x_1:
                        bad_report = True

                    break
                else:
                    no_x = deepcopy(report)
                    no_x.pop(x)

                    no_x_1 = deepcopy(report)
                    no_x_1.pop(x + 1)

                    no_x_m1 = deepcopy(report)
                    no_x_m1.pop(x - 1)

                    no_x = _check_report(no_x, dampened=True)
                    no_x_1 = _check_report(no_x_1, dampened=True)
                    no_x_m1 = _check_report(no_x_m1, dampened=True)
                    if no_x and no_x_1 and no_x_m1:
                        bad_report = True

                    break
            else:
                bad_report = True
                break

        prev_distance = distance

    return bad_report


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    reports = from_txt(__INPUT_FILE)

    good_reports = 0
    for report in reports:
        if not _check_report(report):
            good_reports += 1

    return good_reports


if __name__ == "__main__":
    print(task())
