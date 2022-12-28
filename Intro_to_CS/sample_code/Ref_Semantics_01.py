"""
Small demo of reference semantics for chapter 1 introducing objects
"""

print("=== Example 1: Aliases to a list ===")
x = [1, 2, 3]
y = x
y.append(4)
print(x)
print(y)

print("=== Example 2: Distinct lists  ===")
x = [1, 2, 3]
y = [1, 2, 3]
y.append(4)
print(x)
print(y)

print("=== Example 3: Aliases to a point ===")


class Point:
    """An (x,y) coordinate pair"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy


p1 = Point(3, 5)
p2 = p1
p1.move(4, 4)
print(p1.x, p1.y)
print(p2.x, p2.y)

print("=== Example 4: A method that doesn't mutate ===")


class Point:
    """An (x,y) coordinate pair"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def moved(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)


p1 = Point(3, 5)
p2 = p1
p1 = p1.moved(4, 4)
print(p1.x, p1.y)
print(p2.x, p2.y)
