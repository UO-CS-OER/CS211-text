"""Chapter 1 - composing objects - Rect"""

from numbers import Number


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


class Rect:
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
        return f"Rect({repr(self.min_pt)}, {repr(self.max_pt)}"

    def __str__(self) -> str:
        return f"Rect({str(self.min_pt)}, {str(self.max_pt)})"


p1 = Point(3, 5)
p2 = Point(8, 7)
r1 = Rect(p1, p2)
mvmt = Point(4, 5)
r2 = r1.translate(mvmt)  # Treat Point(4,5) as (dx, dy)
print(f"{r1} + {mvmt} => {r2}")
print(f"Area of {r1} is {r1.area()}")


class RectList:
    """A collection of Rects."""

    def __init__(self):
        self.elements = []

    def area(self) -> Number:
        total = 0
        for el in self.elements:
            total += el.area()
        return total

    def append(self, item: Rect):
        """Delegate to elements"""
        self.elements.append(item)


li = RectList()
li.append(Rect(Point(3, 3), Point(5, 7)))
li.append(Rect(Point(2, 2), Point(3, 3)))
print(f"Combined area is {li.area()}")


class Square(Rect):
    def __init__(self, anchor: Point, size: Number):
        self.min_pt = anchor
        self.max_pt = self.min_pt + Point(size, size)
        self.size = size

    def __str__(self) -> str:
        return f"Square({str(self.min_pt)}, {self.size})"


print("Squares are Rects")
p1 = Point(3, 5)
sq = Square(p1, 5)
print(sq)
s2 = sq.translate(Point(2, 2))
print(s2)
