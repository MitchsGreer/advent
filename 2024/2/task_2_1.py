"""
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

Your puzzle answer was 390.
"""

from copy import deepcopy
from pathlib import Path
from typing import List, Union

__INPUT_FILE = Path(Path(__file__).parent, "task_2_1.txt")


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


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    reports = from_txt(__INPUT_FILE)

    good_reports = 0
    for report in reports:
        bad_report = False

        report_copy = deepcopy(report)
        report_copy.pop()
        report_copy.insert(0, 0)

        distances = list(map(lambda x: x[0] - x[1], zip(report, report_copy)))
        distances = distances[1:]

        if 0 in distances:
            bad_report = True

        if any(map(lambda x: x > 3, list(map(lambda x: abs(x), distances)))):
            bad_report = True

        if distances[0] > 0 and list(map(lambda x: abs(x), distances)) != distances:
            bad_report = True

        if distances[0] < 0 and list(map(lambda x: -abs(x), distances)) != distances:
            bad_report = True

        if not bad_report:
            good_reports += 1

    return good_reports


if __name__ == "__main__":
    print(task())
