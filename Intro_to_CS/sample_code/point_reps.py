"""
Code samples for background reading with
motivation for classes and objects
"""

from typing import Tuple
from numbers import Number
import math

def move_point(p: Tuple[Number, Number],
               d: Tuple[Number, Number]) \
        -> Tuple[Number, Number]:
    x, y = p
    dx, dy = d
    return (x+dx, y+dy)

assert move_point((3,4),(5,6)) == (8,10)

class Point:
    """An (x,y) coordinate pair"""
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    def move(self, d: "Point") -> "Point":
        """(x,y).move(dx,dy) = (x+dx, y+dy)"""
        x = self.x + d.x
        y = self.y + d.y
        return Point(x,y)

    def move_to(self, new_x: int, new_y: int):
        """Change the coordinates of this Point"""
        self.x = new_x
        self.y = new_y

    def distance(self, other: "Point") -> float:
        """Cartesian distance between points"""
        dx = self.x - other.x
        dy = self.y - other.y
        dist_sqr = dx * dx + dy * dy
        return math.sqrt(dist_sqr)

    def __add__(self, other: "Point") -> "Point":
        """(x,y) + (dx, dy) = (x+dx, y+dy)"""
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Rect:
    """A rectangle defined by its lower-left and upper-right corners"""

    def __init__(self, p1: Point, p2: Point):
        """Represented by lower left and upper right corners,
        which might differ from p1 and p2 (e.g., if p1 is above and
        to the right of p2).
        """
        self._ll = Point(min(p1.x, p2.x), min(p1.y, p2.y))
        self._ur = Point(max(p1.x, p2.x), max(p1.y, p2.y))

    def width(self) -> Number:
        return self._ur.x - self._ll.x

    def height(self) -> Number:
        return self._ur.y - self._ll.y

    def area(self) -> Number:
        return self.width() * self.height()

    # Let's define "greater than" as "bigger than", giving a total ordering
    # on rectangles by size.
    # (This is probably a bad idea, but we'll use it rather than
    # starting a new example from scratch.)

    ####
    # Root comparisons <, ==
    ####

    def __lt__(self, other: 'Rect') -> bool:
        "Order rectangles by size"
        return (self.area() < other.area())

    def __eq__(self, other: 'Rect') -> bool:
        return (self.area() == other.area())

    ####
    # Derived comparisons delegate to root comparisons
    # Each makes calls to a magic method for root comparisons
    ####

    def __gt__(self, other: 'Rect') -> bool:
        return other < self

    def __ge__(self, other: 'Rect') -> bool:
        return not (self < other)

    def __le__(self, other: 'Rect') -> bool:
        return  self < other or self == other

####
# Examples with Point class
####

p = Point(3, 4)
v = Point(5, 6)
m = p.move(v)

assert m.x == 8 and m.y == 10

m.move_to(19, 23)

assert m.x == 19 and m.y == 23

p = Point(3, 4)
v = Point(5, 6)
r = p + v

assert r.x == 8 and r.y == 10

print(f"p is ({p.x}, {p.y})")
print(f"p is {p}")
print(f"repr(p) is {repr(p)}")

print("=== str vs repr with lists ===")
print(p)
print(v)
print([p, v])

####
# Examples with Rect class
####

r1 = Rect(Point(1,1), Point(3,3))   # 2x2 rect area = 4
r2 = Rect(Point(2, 2), Point(4, 4)) # 2x2 rect area = 4
r3 = Rect(Point(4,0), Point(5, 2))  # 1x2 rect area = 2

assert r1 == r2
assert r1 != r3
assert r1 > r3
assert r3 < r1
assert r1 >= r2
assert r1 >= r3
assert r1 <= r2
assert r3 <= r1
print("Passed some sanity checks for ordering of rectangles by size")



