"""This file tests each of the tasks in this folder."""

import task_5_1
import task_5_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_5_1.task() == 6051


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_5_2.task() == 5093
