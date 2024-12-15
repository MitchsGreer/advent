These are solutions to the code advent questions from [here](https://adventofcode.com/).

# Structure

They tasks separated by year and task number.

```
2024
  1
    task_1_1.py <- The python source to complete task 1.1.
    task_1_1.txt <- The input text file for task 1.1.
    task_1_2.py
    task_1_2.txt
    test+task_1.py <- The test file with answers for the tasks 1.1 and 1.2.
  2
    ...
  ...
...
```

# Creating a New Task Section

A new task section can be made from the python copier template in `template`. A script has been made at `scripts/task` that will make tasks based on the template with the task name being the basename of the given directory.

Example Usage:

```
#> scripts/task 2024/26
```

This will create a new task at ./2024/26 with the task number 26.

# Testing

Tests exist for code golf. The answer are stored there (spoilers!) and are tested in case any changes are made for efficiency. These tests can be ran with pytest.

```
#> python -m pytest
```
