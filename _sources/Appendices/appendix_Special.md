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
# Appendix -- Magic Methods

Python's *special* methods are also 
known as *dunder* methods, but most
commonly they are referred to as 
*magic* methods.  They are methods 
that are implicitly invoked when 
certain operations are encountered 
(e.g., `a + b` is interpreted as 
`a.__add__(b)`) or when certain 
built-in functions are called 
(e.g., `len(a)` is actually a call 
to `a.__len()`).  The purpose of 
magic methods is to provide a convenient 
way to use simple, familiar 
syntax for both built-in classes 
like `int` and `float` and custom 
classes like `RomanNumerals`. 

## Common Arithmetic Operations

| Operation | Interpreted as  |
|-----------| --------------- |
| `a + b`   | `a.__add__(b)`  |
| `a - b`   | `a.__sub__(b)`  |
| `a * b`   | `a.__mul__(b)`  |
| `a / b`   | `a.__truediv__(b)` |
| `a // b`  | `a.__floordiv__(b)` |
| `a % b`   | `a.__mod__(b)`  |
| `a ** b`  | `a.__pow__(b)`  |

## Augmented Assignment 

Often we use an arithmetic operation 
in combination with assignment, e.g., 
`x += 1` to increment x.  These are 
called *augmented arithmetic assignments*. 
The corresponding methods should 
update the `self` object and return it. 

| Operation  | Interpreted as   |
|------------| ---------------- |
| `a += b`   | `a.__iadd__(b)`  |
| `a -= b`   | `a.__isub__(b)`  |
| `a *= b`   | `a.__imul__(b)`  |
| `a /= b`   | `a.__itruediv__(b)` |
| `a //= b`  | `a.__ifloordiv__(b)` |
| `a %= b`   | `a.__imod__(b)`  |
| `a **= b`  | `a.__ipow__(b)`  |

## Comparisons 

The comparison methods should return 
a result of type `bool`.  They are also 
called *rich comparison methods*. 

| Operation  | Interpreted as   |
|------------| ---------------- |
| `a < b`    | `a.__lt__(b)`    |
| `a <= b`   | `a.__le__(b)`    |
| `a == b`   | `a.__eq__(b)`    |
| `a > b`    | `a.__gt__(b)`    |
| `a >= b`   | `a.__ge__(b)`    |

A `__ne__` method may also be implemented 
to perform the `!=` operation, but typically 
it is omitted.  If a class does not have 
a `__ne__` method, Python will interpret 
`a != b` by calling `a.__eq__(b)` and 
inverting the result.  

*No other relations among comparisons are 
guaranteed.*   For example, if you provide
a `__lt__` and a `__eq__` method for a class, 
you still need a `__le__` method if you 
want to be able to write `a <= b`.  Also, 
it is possible that `a.__lt__(b)` and 
`b.__lt__(a)` both return True, although 
this is likely to be a very bad idea. 

Although Python does not assume any relationships among comparisons 
like `<=`, `<`, and `==`, you don't need to implement each 
independently.  Suppose, for example, that you are defining a class 
of objects that are ordered by size.  You might have 

## Built-in Functions

Although listed in Python documentation 
as built-in functions, these are really
calls to methods that are defined in all 
the built-in classes.  

| Function call | Interpreted as  |
|---------------| --------------- |
| `abs(x)`      | `x.__abs__()`   |
| `int(x)`      | `x.__int__()`   |
| `float(x)`    | `x.__float__()` |
| `str(x)`      | `x.__str__()`   |
| `repr(x)`     | `x.__str__()`   |

Note that `str` and `repr` are often 
called implicitly.  When we write 
`f"The value of x is {x}"`, the 
`{x}` in the f-string is an implicit call to 
`str(x)` (and therefore an implicit
call to `x.__str__()`).  When we 
type `x + y` in the Python console, 
Python first calls `x.__add__(y)`, 
and then calls `repr` on the result 
to print it, so what is actually 
printed at the console is 
`x.__add__(y).__repr__()`. 

## Collection Operations

Python provides convenient notation 
for collections.  For example, if 
`d` is a `dict` objects, we can 
write 
`d[k]=v` to add the pair `(k,v)`
`d` (replacing `(k,w)` if 
the key `k` was previously associated 
with `w`).  These operations are 
also implemented by magic methods. 
We can implement those methods in 
other ways to create custom 
collection classes. 

| Operation | Interpreted as   |
| --------- | ---------------- |
| `len(c)`  | `c.__len__()`    |
| `_ = c[k]`| `c.__getitem__(k)` |
| `c[k] = v`| `c.__setitem__(k,v)` |
| `k in c`  | `c.__contains__(k)`|

Python also lets us write 
`for v in c:` or `for k,v in c:` 
to loop through items in a 
collection.  This involves creation 
of an *iterator* object. If we have 

```python
for k in c: 
   (do something with k)
```

this is interpreted as 

```python
i = c.__iter()__ 
try
  while True: 
     k = i.__next__()
     (do something with k)
except StopIteration: 
  pass
```

When we build a *wrapper* class 
for a collection, in the object 
*wraps* another collection, 
we can often avoid the complication of 
writing a custom iterator class (the type 
of the object returned by `__iter__`)
and just *delegate* to the iterator of 
the wrapped class.  For example: 

```python
class Menagerie: 
   """A list of animals"""
   def __init__(self):
        self.animals = []

   def __iter__(self):
        return self.animals.__iter__()
```

## Additional magic methods 

I have listed only the most common 
magic methods, leaving out some 
that we are unlikely to encounter 
in a introductory course.  A more complete list, 
with additional documentation can be 
found in the 
[*data model* chapter](https://docs.python.org/3/reference/datamodel.html#special-method-names)
of the official Python documentation. 