---
jupytext:
  formats: md:myst
  text_representation:
    extension: .myst
    format_name: myst
    format_version: 1.1
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Objects 

In Python, objects are used to represent 
information.  Every variable you use in a Python 
program is a reference to an object.
The values you have been using so far – 
numbers, strings, dicts, lists, etc – are objects. 
They are among the built-in classes of Python, 
i.e., kinds of value that are already defined 
when you start the Python interpreter.  

You are not limited to those built-in classes. 
You can use them as a foundation to build your 
own. 

## Example: Points

What if we wanted to define a new kind of value?
For example, if we wanted to write a program 
to draw a graph, we might want to work with 
cartesian coordinates, representing each 
point as an (x,y) pair.  We might represent the 
point as a tuple like `(5,7)`, or we could represent 
it as the list `[5, 7]`, or we could represent
it as a dict `{"x": 5, "y": 7}`, and that 
might be satisfactory.   If we wanted to represent moving a point (x,y)
by some distance (dx, dy), we could define a a function like 

```{code-cell} python3
def move(p, d):
    x,y = p
    dx, dy = d
    return (x+dx, y+dy)
    
pt_1 = (5,8)
pt_2 = move(pt_1, (3,7))
print(pt_2)
```

But if we are making a graphics program, we'll need  *move*
functions for other graphical objects like rectangles and ovals, 
so instead of naming it `move` we'll need a more descriptive name 
like `move_point`.  Also we should give the type contract for 
the function, which we can do with Python type hints.  With these 
changes, we get something like this

```{code-cell} python3
from typing import Tuple
from numbers import Number

def move_point(p: Tuple[Number, Number],
               d: Tuple[Number, Number]) \
        -> Tuple[Number, Number]:
    x, y = p
    dx, dy = d
    return (x+dx, y+dy)
    
move_point((3,4),(5,6))
```

### Can we do better? 

We aren't really satisfied with using tuples to 
represent points.  What we'd really 
like is to express the concept of adding two points 
more concisely, as `(3,4) + (5,6)`.  What would happen if we 
tried this? 

```{code-cell} python3
(3,4) + (5,6)
```

That's not what we wanted!  Would it be better if we represented 
points as lists? 

```{code-cell} python3 
[3,4] + [5,6]
```

No better.  Maybe as dicts? 

```{code-cell} python3
:tags: [raises-exception]

{"x": 3, "y": 4} + {"x": 5, "y": 6}
```

That is not much of an improvement, although 
an error message is usually better than silently 
producing a bad result. What we really
want is not to use one of the 
existing representations like lists or tuples or dicts, 
but to define a new representation for points.  

### A new representation

Each data type in Python, including list, tuple, 
and dict, is defined as a *class* from which 
*objects* can be constructed.  We can also define 
our own classes, to construct new kinds of objects.   
For example, we can make a new class `Point` to 
represent points.  

```python
class Point:
    """An (x,y) coordinate pair"""
```

Inside the class we can define *methods*, which are like functions 
that are specialized for the new representation.   The first 
method we should define is a *constructor* with the name `__init__`. 
The constructor describes how to create a new `Point` object: 

```{code-cell} python3
class Point:
    """An (x,y) coordinate pair"""
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y
        
p = Point(5,3)

print(f"p has x coordinate {p.x} and y coordinate {p.y}")
```

### Instance variables 

Notice that the first argument to the constructor method is 
`self`, and within the method we refer to `self.x` and `self.y`.
In a method that operates on some object *o*, the first argument
to the method will always be `self`, which refers to the whole 
object *o*.   Within the `self` object we can store *instance 
variables*, like `self.x` and `self.y` 
for the *x* and *y* coordinates of a point.
When we use the Point object `p` from outside the class,
we refer to those elements as `p.x` and `p.y`, as in the
print statement above. 

### Methods

What about defining an operation for moving a point?  Instead of 
adding `_point` to the name of a `move` function, we can just 
put the function (now called a *method*) *inside* the `Point` 
class:

```{code-cell} python3
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
```

Notice that the *instance variables* 
`self.x` and `self.y` we created in the constructor 
can be used in the `move` method.  They are part of 
the object, and can be used by any method in the class.
The instance variables of the other `Point` object `d` 
are also available 
in the `move` method.  Let's look at how these objects 
are passed to the `move` method. 

### Method calls

Next we'll create two `Point` objects and call the `move` method 
to create a third `Point` object with the sums of their *x* and 
*y* coordinates: 

```{code-cell} python3
p = Point(3,4)
v = Point(5,6)
m = p.move(v)

print(f"m has x coordinate {m.x} and y coordinate {m.y}")
```

At first it may seem confusing that we defined the ```move``` method with two arguments, `self` and `d`, but 
it looks like we passed it only one argument, `v`.  In fact 
we passed it both points:  `p.move(v)` passes `p` as the `self` argument and `v` as the `d` argument.  We use the variable 
before the `.`, like `p` in this case, in two different ways: To find the right method (function) to call, by looking inside the *class* to 
which `p` belongs, and to pass as the `self` argument to the method.

The `move` method above returns a new `Point` object at the 
computed coordinates.  A method can also change the values of 
instance variables.   For example, suppose we add a `move_to` 
method to `Point`: 

```{code-cell} python3
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
        
    def move_to(self, new_x, new_y):
        """Change the coordinates of this Point"""
        self.x = new_x
        self.y = new_y

m = Point(3,4)
m.move_to(19,23)
print(f"({m.x}, {m.y})")
```

Note that the `move_to` method does _not_
return the moved point.  This is a common mistake! 

```{code-cell} python3
:tags: [raises-exception]

w = m.move_to(19, 23)  # Oops! 
print(w)

# Attempting to access w.x or w.y will fail: 
print(f"w has x coordinate {w.x} and y coordinate {w.y}")
```

### What is `self`?

Many people are confused by the `self` variable.  The name `self` is 
merely a convention in Python.  Conventions are important for 
readability and avoiding errors, so you should never write code 
like the following, but it may help you to see that there is really 
nothing special about `self` aside from convention. 

```{code-cell} python3
class BadExample():
    """An example in which we use other names instead of "self".
    DON'T DO THIS ... but understand it. 
    """
    
    def __init__(elephant, x: int): 
        elephant.v = x    # Might as well be consistently inconsistent
        
    def increase(zebra, y: int): 
        zebra.v += y
        
wacky = BadExample(17)
wacky.increase(13)
print(wacky.v)
```

As you can see, when we make a method call like `wacky.increase(13)`,
the first argument is the object `wacky`.  We ordinarily call that 
argument `self`, not because it matters to Python, but because it 
matters to other programmers who need to read and understand our code. 

### *Check your understanding*

Consider class `Pet` and object `my_pet`.  
What are the *instance variables* of `my_pet`? 
What are the values of those instance variables 
after executing the code below? 

```python
class Pet: 
    def __init__(self, kind: str, name: str):
        self.species = kind
        self.called = name
    
    def rename(self, new_name):
        self.called = new_name

my_pet = Pet("canis familiaris", "fido")
```


## Combining Objects: Composing

The *instance variables* defined in a class and stored 
in the objects of that class can themselves be objects. 
We can make lists of objects, tuples of objects, etc. 

Often we will want to create a new class with instance 
variables that are objects created from classes that 
we have previously created.  For example, if we create a 
new class `Rect` to represent rectangles, we might want
to use `Point` objects to represent two corners of 
the rectangle: 

```{code-cell} python3
:tags:  [  "hide-cell" ]

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
        
    def move_to(self, new_x, new_y):
        """Change the coordinates of this Point"""
        self.x = new_x
        self.y = new_y
        
    def __add__(self, other: "Point"):
        """(x,y) + (dx, dy) = (x+dx, y+dy)"""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        """Printed representation.
        str(p) is an implicit call to p.__str__()
        """
        return f"({self.x}, {self.y})"
      
    def __repr__(self) -> str:
        """Debugging representation.  This is what
        we see if we type a point name at the console.
        """
        return f"Point({self.x}, {self.y})"
```  

```{code-cell} python3
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

p1 = Point(3,5)
p2 = Point(8,7)
r1 = Rect(p1, p2)
mvmt = Point(4, 5)
r2 = r1.translate(mvmt)  # Treat Point(4,5) as (dx, dy)
print(f"{r1} + {mvmt} => {r2}")
print(f"Area of {r1} is {r1.area()}")
```

Note that the `height` and `width` are local variables 
that exist only while method `area` is executing. 
`min_pt` and `max_pt`, on the other hand, are 
*instance variables* that are stored within the 
`Rect` object.  

### *Check your understanding*

Suppose we ran the above code in PythonTutor. 
(PythonTutor cannot import `Number`, but for the examples we could 
replace it with `int`.)  What picture would it draw 
of `r1`?   Would `height` and `width` in method 
`area` be included as instance variables?  Why or 
why not?  


## Wrapping and delegation

Sometimes we want a class of objects that is almost
like an existing class, but with a little extra 
information or a few new methods.  One way to do this 
is to build a new class that _wraps_ an existing class, 
often a built-in class like `list` or `dict`.  (In
[the next chapter](02_Inheritance/02_1_Inheritance.md) we will 
see another approach.)

Suppose we wanted objects that provide some of the same 
functionality as `list` objects, and also some new 
functionality or some restrictions.  For example, we 
might want a method `area` that returns the sum of 
the areas of all the `Rect` objects in the `RectList`: 

```{code-cell} python3
class RectList:
    """A collection of Rects."""

    def __init__(self):
        self.elements = [ ]

    def area(self) -> Number:
        total = 0
        for el in self.elements:
            total += el.area()
        return total
```

That seems reasonable, but how do we add `Rect` objects to the 
`Rectlist`? 

We do *not* want to do it this way: 

```python3
li = RectList()
# DON'T DO THIS
li.elements.append(Rect(Point(3,3), Point(5,7)))
li.elements.append(Rect(Point(2,2), Point(3,3)))
```

As a general rule, we should be cautious about accessing the instance 
variables of an object outside of methods of the object's class, 
and we should especially avoid modifying instance variables anywhere 
except in methods.  Code that "breaks the abstraction", like the example
above calling the `append` method of the `elements` instance variable, is 
difficult to read and maintain. So we want instead to give `RectList`
it's own `append` method, so that we can write 

```python3
li = RectList()
li.append(Rect(Point(3,3), Point(5,7)))
li.append(Rect(Point(2,2), Point(3,3)))
print(f"Combined area is {li.area()}")
```
  
The `append` method can be very simple! 

```python
    def append(self, item: Rect):
        """Delegate to elements"""
        self.elements.append(item)
```

```{code-cell} python3
:tags: [hide-cell]
class RectList:
    """A collection of Rects."""

    def __init__(self):
        self.elements = [ ]
        
    def append(self, item: Rect):
        """Delegate to elements"""
        self.elements.append(item)

    def area(self) -> Number:
        total = 0
        for el in self.elements:
            total += el.area()
        return total
```

```{code-cell} python3
li = RectList()
li.append(Rect(Point(3,3), Point(5,7)))
li.append(Rect(Point(2,2), Point(3,3)))
print(f"Combined area is {li.area()}")
```

We call this *delegation* because `append` method of `RectList` method  
just hands off the work to the `append` method of class `list`.  When we 
write a *wrapper* class, we typically write several such 
trivial *delegation* methods.   

Wrapping and delegation work well when we want the wrapper class 
(like `RectList` in this example) to
have a few of the same methods as the wrapped class (`list`).  When 
we want the new collection class to have all or nearly all the methods 
of an existing collection, the *inheritance* approach introduced in the 
next chapter is more appropriate. 