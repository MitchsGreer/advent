"""This file tests each of the tasks in this folder."""

import task_1_1
import task_1_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_1_1.task() == 2285373


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_1_2.task() == 21142653
