"""
Examples of functional programming in Python.

(These examples are for demonstration purposes
and do not use the 'functools' library.  If you
want to use functional techniques in a project,
you should check out the 'functools' library
and use it in preference to reimplementing your
own versions of what it provides.)
"""
from typing import List, Callable, Optional

"""Reduce is a generalization of sum. It applies 
a binary operation like plus or times to elements 
of a list. To keep it simple, I will define a 'reduce' 
function that works on lists of int.  A more generic 
version that works on other lists is possible, but 
the type hints are more complicated. 
"""


def reduce(l: List[int], initial: int, f: Callable[[int], int]) -> int:
    """ Reduce l by f, i.e., f(el, f(el, f(el, ...))) for el in l"""
    reduction = initial
    for el in l:
        reduction = f(reduction, el)
    return reduction


li = [1, 2, 3, 4, 5]

# Reduce with + is same as sum
assert reduce(li, 0, lambda a, b: a + b) == 15

# Reduce with * is product of all elements
assert reduce(li, 1, lambda a, b: a * b) == 120

# Trickier!  We can also get a 'count' function
assert reduce(li, 0, lambda a, b: a + 1) == 5


# Max, min, or some other selection
def larger(x, y):
    """For demo purposes only; built-in max is preferable"""
    if x > y: return x
    return y


assert reduce(li, li[0], larger) == 5

"""Binary tree traversal with a function argument"""


class Tree:
    """The abstract base class"""

    def reduce(self, f: Callable[[int, int], int],
               leaf_val: Optional[int] = None):
        """f is a function for combining values of subtrees.
        Leaves will return their own value unless leaf_val
        is specified.
        """
        raise NotImplementedError("Each subclass must implement reduce")


class Leaf(Tree):
    def __init__(self, val: int):
        self.val = val

    def reduce(self, f: Callable[[int, int], int],
               leaf_val: Optional[int] = None):
        if leaf_val is None:
            return self.val
        else:
            return leaf_val


class Inner(Tree):
    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def reduce(self, f: Callable[[int, int], int],
               leaf_val: Optional[int] = None):
        return f(self.left.reduce(f, leaf_val),
                 self.right.reduce(f, leaf_val))


t = Inner(Inner(Leaf(1), Leaf(2)),
          Inner(Leaf(3), Inner(Leaf(4), Leaf(5))))

# Sum leaves of tree
assert t.reduce(lambda v, w: v + w) == 15
# Product of leaves of tree
assert t.reduce(lambda v, w: v * w) == 120
# Max/Min leaf of tree using built-in max and min
assert t.reduce(max) == 5
assert t.reduce(min) == 1
# Count leaves
assert t.reduce(lambda x, y: x + y, leaf_val=1) == 5
