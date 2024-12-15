"""This file tests each of the tasks in this folder."""

import task_4_1
import task_4_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_4_1.task() == 2458


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_4_2.task() == 1945
