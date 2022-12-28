"""
Samples for chapter 3, recursion in the OO style
"""
from typing import List, Tuple

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


# Classic factorial, before simplifying

def classic_factorial(value: int) -> int:
    """We always check base cases first"""
    if value < 2:
        return 1
    else:
        """Recursive case(s) follow"""
        p1 = value - 1
        r1 = classic_factorial(p1)
        return value * r1


assert classic_factorial(5) == 120


def fact(value: int) -> int:
    if value < 2:
        return 1
    return value * fact(value - 1)


assert fact(5) == 120


def bin_search(key: int, table: List[Tuple[int, str]]) -> str:
    return bin_search_range(key, table, 0, len(table) - 1)


def bin_search_range(key: int, table: List[Tuple[int, str]],
                     low: int, high: int) -> str:
    """Recursive binary search in range low..high inclusive"""

    """Base case 1: Key is not in table"""
    if low > high:
        return "No such value"

    mid = (high + low) // 2
    entry_key, entry_value = table[mid]

    """Base case 2: Key found at midpoint in table"""
    if entry_key == key:
        return entry_value

    if key < entry_key:
        """Recursive case 1: Key must be before midpoint, or absent"""
        return bin_search_range(key, table, low, mid - 1)

    else:
        """Recursive case 2: Key must be after midpoint, or absent"""
        return bin_search_range(key, table, mid + 1, high)


table = [(1, "alpha"), (3, "beta"), (4, "gamma"), (9, "delta"), (12, "epsilon"), (15, "zeta")]
assert bin_search(1, table) == "alpha"
assert bin_search(0, table) == "No such value"
assert bin_search(2, table) == "No such value"
assert bin_search(3, table) == "beta"
assert bin_search(4, table) == "gamma"
assert bin_search(5, table) == "No such value"
assert bin_search(8, table) == "No such value"
assert bin_search(9, table) == "delta"
assert bin_search(11, table) == "No such value"
assert bin_search(12, table) == "epsilon"
assert bin_search(15, table) == "zeta"
assert bin_search(17, table) == "No such value"

nested = [4, "gamma",
          [3, "beta",
           [1, "alpha", [], []],
           []],
          [12, "epsilon",
           [9, "delta", [], []],
           [15, "zeta", [], []]]
          ]


def nested_list_search(key: int, table: list) -> str:
    """Table is [key, value, smaller keys, larger keys]"""
    log.debug(f"Search for {key} in {table}")
    """Base case 1: There are no keys"""
    if table == []:
        return "No such value"

    entry_key, entry_value, smaller, larger = table
    """Base case 2: Key is found"""
    if key == entry_key:
        return entry_value

    if key < entry_key:
        """Recursive case 1: Must be in the smaller keys"""
        return nested_list_search(key, smaller)
    else:
        """Recursive case 2: Must be in the larger keys"""
        return nested_list_search(key, larger)


# assert nested_list_search(1, nested) == "alpha"
assert nested_list_search(0, nested) == "No such value"
assert nested_list_search(1, nested) == "alpha"
assert nested_list_search(2, nested) == "No such value"
assert nested_list_search(3, nested) == "beta"
assert nested_list_search(4, nested) == "gamma"
assert nested_list_search(5, nested) == "No such value"
assert nested_list_search(8, nested) == "No such value"
assert nested_list_search(9, nested) == "delta"
assert nested_list_search(11, nested) == "No such value"
assert nested_list_search(12, nested) == "epsilon"
assert nested_list_search(15, nested) == "zeta"
assert nested_list_search(17, nested) == "No such value"


class GreekSearchTree:
    """An abstract base class for the table of Greek letters"""

    def __init__(self):
        raise NotImplementedError("Nope, can't do that")

    def search(self, key: int) -> str:
        """Return associated string or 'No such value'"""
        raise NotImplementedError("Concrete classes must override the search method")


class Node(GreekSearchTree):
    def __init__(self, key: int, value: str, smaller: GreekSearchTree, larger: GreekSearchTree):
        self.key = key
        self.value = value
        self.smaller = smaller
        self.larger = larger

    def search(self, key) -> str:
        if self.key == key:
            return self.value
        if key < self.key:
            return self.smaller.search(key)
        else:
            return self.larger.search(key)


class Empty(GreekSearchTree):
    def __init__(self):
        pass

    def search(self, key) -> str:
        return "No such value"


# The leaves
empty = Empty()  # I really only need one of these
alpha = Node(1, "alpha", empty, empty)
delta = Node(9, "delta", empty, empty)
zeta = Node(15, "zeta", empty, empty)
# The internal nodes
beta = Node(3, "beta", alpha, empty)
epsilon = Node(12, "epsilon", delta, zeta)
gamma = Node(4, "gamma", beta, epsilon)
# (4, gamma) is at the root
tree = gamma

assert tree.search(4) == "gamma"
assert tree.search(3) == "beta"
assert tree.search(1) == "alpha"
assert tree.search(12) == "epsilon"
assert tree.search(9) == "delta"
assert tree.search(15) == "zeta"
assert tree.search(0) == "No such value"
assert tree.search(5) == "No such value"
assert tree.search(11) == "No such value"
assert tree.search(17) == "No such value"

print("Tests ok")
