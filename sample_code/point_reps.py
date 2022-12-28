"""
Code samples for background reading with
motivation for classes and objects
"""

from typing import Tuple
from numbers import Number

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

    def __add__(self, other: "Point") -> "Point":
        """(x,y) + (dx, dy) = (x+dx, y+dy)"""
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


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
