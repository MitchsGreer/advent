"""
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

    75,97,47,61,53 becomes 97,75,47,61,53.
    61,13,29 becomes 61,29,13.
    97,13,75,29,47 becomes 97,75,47,29,13.

After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""

from pathlib import Path
from typing import List, Tuple, Union

__INPUT_FILE = Path(Path(__file__).parent, "task_5_2.txt")


def from_txt(input_file: Union[Path, str]) -> Tuple[List[List[int]], List[List[int]]]:
    """Import challenge input from a `.txt`.

    Args:
        input_file: The input filepath.

    Returns:
        The input data.
    """
    rules = []
    page_orders = []
    with open(input_file) as in_file:
        for line in in_file.readlines():
            line = line.strip()

            if "|" in line:
                rules.append(list(map(int, line.split("|"))))
            elif "," in line:
                page_orders.append(list(map(int, line.split(","))))

    return rules, page_orders


def _check_page_order(rules: List[List[int]], page_order: List[int]) -> int:
    """Check the page order matches the given rules.

    Args:
        rules: The rules to match, a list of lists of 2 elements.
        page_order: The list of page orders to check.

    Returns:
        The middle page number if the pages are in the correct order, 0 otherwise.
    """
    follows_rules = True
    middle_page_num = 0
    for rule in rules:
        try:
            page_1_index = page_order.index(rule[0])
            page_2_index = page_order.index(rule[1])

            if page_1_index > page_2_index:
                follows_rules = False
                page_order = _reorder_pages(rules, page_order)
                break

        except ValueError:
            pass  # We ignore rules that are not in the list.

    if not follows_rules:
        middle_page_num = page_order[(len(page_order) // 2)]

    return middle_page_num


def _reorder_pages(rules: List[List[int]], page_order: List[int]) -> List[int]:
    """Reorder the given page number with the given rules.

    Args:
        rules: The rules to order with.
        page_order: The pages to order.

    Returns:
        The new order to the pages.
    """
    relevant_rules = []

    for rule in rules:
        if rule[0] in page_order and rule[1] in page_order:
            relevant_rules.append(rule)

    edge_list = {}
    for page in page_order:
        edge_list[page] = 0

    for rule in relevant_rules:
        edge_list[rule[1]] += 1

    edge_tuples = list(edge_list.items())
    edge_tuples.sort(key=lambda x: x[1])

    new_order = [page[0] for page in edge_tuples]

    return new_order


def task() -> int:
    """Complete the task and return the answer.

    Returns:
        The answer to task.
    """
    rules, page_orders = from_txt(__INPUT_FILE)

    sum_mid_pages = 0
    for page_order in page_orders:
        sum_mid_pages += _check_page_order(rules, page_order)

    return sum_mid_pages


if __name__ == "__main__":
    print(task())
