"""
Chapter 2, Inheritance: 'shape.py'
Extension of the 'rect.py' basic demo code,
this time making a rectangle be one of the
subclasses of an abstract class Shape.
"""

from numbers import Number
from math import sqrt


class Point:
    """An (x,y) coordinate pair"""

    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    def __add__(self, other: "Point"):
        """(x,y) + (dx, dy) = (x+dx, y+dy)"""
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def dist(self, other: "Point") -> Number:
        """Euclidean distance = sqrt(dx^2 + dy^2)"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)


class Shape:
    """An abstract base class that encompasses different concrete
    classes with common behavior but different representations.
    """

    def __init__(self):
        """There are *no* objects of an abstract class.  It's a
        concept, not a set of concrete things.
        """
        raise NotImplementedError("Do not instantiate 'Shape'; it is abstract")

    # Methods of abstract methods are mostly to define signatures
    # (headers) of methods for the concrete subclasses

    def area(self) -> Number:
        raise NotImplementedError(f"Class {self.__class__} didn't define 'Area'")

    def translate(self, delta: Point) -> "Shape":
        """New shape offset from this one by delta as movement vector"""
        raise NotImplementedError(f"Class {self.__class__} didn't define 'translate'")


class Rect(Shape):
    """A rectangle is represented by a pair of points
    (x_min, y_min), (x_max, y_max) at opposite corners.
    Whether (x_min, y_min) is lower left or upper left
    depends on the coordinate system.
    """

    def __init__(self, xy_min: Point, xy_max: Point):
        self.min_pt = xy_min
        self.max_pt = xy_max

    def area(self) -> Number:
        """Area is height * width"""
        height = self.max_pt.x - self.min_pt.x
        width = self.max_pt.y - self.min_pt.y
        return height * width

    def translate(self, delta: Point) -> "Rect":
        """New rectangle offset from this one by delta as movement vector"""
        return Rect(self.min_pt + delta, self.max_pt + delta)

    def __repr__(self) -> str:
        return f"Rect({repr(self.min_pt)}, {repr(self.max_pt)})"

    def __str__(self) -> str:
        return f"Rect({str(self.min_pt)}, {str(self.max_pt)})"


class ShapeList(list):
    """A collection of Shapes."""

    def area(self) -> Number:
        total = 0
        for el in self:
            total += el.area()
        return total


class Square(Rect):
    def __init__(self, anchor: Point, size: Number):
        self.min_pt = anchor
        self.max_pt = self.min_pt + Point(size, size)
        self.size = size

    def side(self) -> Number:
        return self.size

    def translate(self, delta: Point) -> "Square":
        return Square(self.min_pt + delta, self.size)

    def __str__(self) -> str:
        return f"Square({self.min_pt}, {self.size})"

    def __repr__(self) -> str:
        return f"Square({repr(self.min_pt)}, {self.size})"


# Triangles are a kind of shape, but the implementation of Rect
# is not helpful ... they aren't defined by two corners, and their
# area is a bit more complex to compute.

# For area of a triangle, (1/2)*base*height,
# I'm going to need height.  Fortunately I've got this
# code lying around from a project that computed distance
# from a path on a map.  I'll

def normal_intersect(p1_x, p1_y, p2_x, p2_y, px, py):
    """
    Find the point at which a line through seg_p1,
    seg_p2 intersects a normal dropped from p.
    """

    # Special cases: slope or normal slope is undefined
    # for vertical or horizontal lines, but the intersections
    # are trivial for those cases
    if p2_x == p1_x:
        return p1_x, py
    elif p2_y == p1_y:
        return px, p1_y

    # The slope of the segment, and of a normal ray
    seg_slope = (p2_y - p1_y) / (p2_x - p1_x)
    normal_slope = 0 - (1.0 / seg_slope)

    # For y=mx+b form, we need to solve for b (y intercept)
    seg_b = p1_y - seg_slope * p1_x
    normal_b = py - normal_slope * px

    # Combining and subtracting the two line equations to solve for intersect
    x_intersect = (seg_b - normal_b) / (normal_slope - seg_slope)
    y_intersect = seg_slope * x_intersect + seg_b
    # Colinear points are ok!

    return (x_intersect, y_intersect)


class Triangle(Shape):
    """A triangle is defined by three points."""

    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def translate(self, delta: Point) -> "Triangle":
        return Triangle(self.p1 + delta, self.p2 + delta, self.p3 + delta)

    def __str__(self) -> str:
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    def __repr__(self) -> str:
        return f"Triangle({repr(self.p1)}, {repr(self.p2)}, {repr(self.p3)})"

    def area(self) -> Number:
        """Area of triangle is (1/2) * base * height"""
        # To determine height, we drop a perpendicular from one point
        # to the opposite side, then measure it.  Any side will do;
        # we'll take p1 as the point and (p2,p3) as the side.
        ix, iy = normal_intersect(self.p2.x, self.p2.y,
                                  self.p3.x, self.p3.y,
                                  self.p1.x, self.p1.y)
        intercept = Point(ix, iy)
        base = self.p2.dist(self.p3)
        height = self.p1.dist(intercept)
        return 0.5 * base * height


def darn_close(n: Number, m: Number, sigma: int = 3):
    """Within 10^(-sigma), default is
    sigma=3 or 1/1000
    """
    fudge = 1.0
    for precision in range(sigma):
        fudge = fudge / 10.0
    return abs(n - m) <= fudge


def triangle_tests():
    """Better test with triangles in different orientations,
    but we need triangles for which it is easy to calculate
    expected area by other means.
    """
    # A simple right triangle --- easy to calculate
    rt = Triangle(Point(0, 0), Point(0, 1), Point(2, 0))
    assert darn_close(rt.area(), 1.0), "Right triangle size should be 1"

    # Should be the same if I reorder the points
    rt = Triangle(Point(0, 1), Point(0, 0), Point(2, 0))
    assert darn_close(rt.area(), 1.0), "Right triangle size should still be 1"

    # Should be the same if I rotate it 45 degrees
    rt = Triangle(Point(sqrt(2.0), sqrt(2.0)), Point(0, 0),
                  Point(1.0 / sqrt(2.0), -1.0 / sqrt(2.0)))
    assert darn_close(rt.area(), 1.0), "Rotated size should still be 1"

    # And again if I nudge it off (0,0)
    rt = rt.translate(Point(3.0, 3.0))
    assert darn_close(rt.area(), 1.0), "Nudged and rotated should still be 1"
    print("Triangle tests passed")


def smoke_test():
    print("=== Smoke test ===")
    # Basic tests for Rect
    p1 = Point(3, 5)
    p2 = Point(8, 7)
    r1 = Rect(p1, p2)
    mvmt = Point(4, 5)
    r2 = r1.translate(mvmt)  # Treat Point(4,5) as (dx, dy)
    print(f"{r1} + {mvmt} => {r2}")
    print(f"Area of {r1} is {r1.area()}")
    # ShapeList is a list of Shape objects
    li = ShapeList()
    li.append(Rect(Point(3, 3), Point(5, 7)))  # 2x4 = 8
    li.append(Square(Point(2, 2), 2))  # 2x2 = 4
    li.append(Triangle(Point(0, 0), Point(0, 1), Point(2, 0)))  # Area 1
    print(f"ShapeList {li}")
    print(f"Combined area is {li.area()}, expecting 13")
    # Basic tests for Square
    print("Squares are Rects")
    p1 = Point(3, 5)
    sq = Square(p1, 5)
    print(f"Square from {p1} side {sq.side()}, {repr(sq)} prints as {sq}")
    s2 = sq.translate(Point(2, 2))
    print(f"{sq} nudged (2,2) is {s2}")
    print("Triangle area tests")
    triangle_tests()


if __name__ == "__main__":
    smoke_test()
