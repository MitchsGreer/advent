"""This file tests each of the tasks in this folder."""

import task_7_1
import task_7_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_7_1.task() == 1582598718861


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_7_2.task() == 165278151522644
