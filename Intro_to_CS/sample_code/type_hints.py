"""Example of using simple, composite, and incomplete type hints"""

from typing import Tuple, List, Dict


def i_eat_tuples(t: Tuple[str, int]) -> Tuple[int, Tuple[int, int]]:
    the_string, the_int = t
    return (the_int, (the_int, the_int))


def to_dict(ls: List[Tuple[str, int]]) -> Dict[str, int]:
    result = {}
    for key, value in ls:
        result[key] = value
    return result


assert i_eat_tuples(("three", 3)) == (3, (3, 3))
assert to_dict([("a", 1), ("b", 2)]) == {"a": 1, "b": 2}
