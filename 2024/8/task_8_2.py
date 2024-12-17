"""
"""

from pathlib import Path
from typing import Union

__INPUT_FILE = Path(Path(__file__).parent, "task_8_1.txt")


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


if __name__ == "__main__":
    print(task())
