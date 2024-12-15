"""This file tests each of the tasks in this folder."""

import task_3_1
import task_3_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_3_1.task() == 188116424


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_3_2.task() == 104245808
