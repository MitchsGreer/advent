"""This file tests each of the tasks in this folder."""

import task_6_1
import task_6_2


def test_task_1_1() -> None:
    """Test that task 1.1 is correct."""
    assert task_6_1.task() == None


def test_task_1_2() -> None:
    """Test that task 1.2 is correct."""
    assert task_6_2.task() == None
