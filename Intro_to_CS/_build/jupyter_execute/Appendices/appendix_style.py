#!/usr/bin/env python
# coding: utf-8

# # Style Guide for Python Programs
# 
# Most software development organizations have coding guidelines that
# constitute a _house style_. These may be based on some more widely used
# standard, but often they will also incorporate norms and preferences
# developed by a particular organization. Students who took CIS 210 at UO
# have used a style guide for that course, based on
# [PEP 8](https://www.python.org/dev/peps/pep-0008/) and extended with
# some additional rules suited to an introductory course.
# 
# Guidelines for CIS 211 projects are also based on
# [PEP 8](https://www.python.org/dev/peps/pep-0008/), but they differ in
# some ways from those used in CIS 210. The key differences are that CIS
# 211 style is designed to be more concise.
# 
# ## Living Document
# 
# This document represents my best effort at defining style guidelines for
# CIS 211, but like many software documents it requires regular revision.
# We may find that we need some additional rules, or that some existing
# rules are annoyingly strict, or that something is not as clear as it
# should be. Also I make mistakes. Students are encouraged to suggest
# revisions. Meanwhile, the standard for any particular project is the
# version of this document as of the project due date. If the guidelines
# change between distribution of a project and its due date, I will use
# Piazza to announce whether the change applies to the current project,
# and to the extent possible I will avoid making you revise projects that
# have already been started.
# 
# ## Basics: When in doubt, follow PEP 8
# 
# [PEP 8](https://www.python.org/dev/peps/pep-0008/)
# is a widely used standard for Python code. It provides guidelines for
# all variety of matters from indentation to spacing in expressions.
# 
# Note in particular that we will follow PEP8 naming conventions,
# including `lower_case` for variables, functions, and methods,
# `CamelCase` for classes, and `SHOUTS` for global constants.
# 
# PEP 8 recommends a maximum line length of 79 characters.  
# This matters!  The human eye has limited accuracy as it moves from the
# end of one line of text to the beginning of the next line. 79 is not a
# magic number (accuracy depends on many other factors, such as vertical
# space between lines), but under typical circumstances it is
# approximately the length at which readers begin to have trouble finding
# the beginning of the correct next line.
# 
# PEP 8 refers to
# [PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstring
# conventions. We will also follow PEP 257 conventions. We will _not_
# specify function and method type signatures in docstrings (see below for
# the alternative), but when appropriate we may use docstring comments to
# say more about arguments and return values.
# 
# ## Function and method headers
# 
# We will use Python
# [type annotations](https://www.python.org/dev/peps/pep-0484/)
# (also known as _type hints_) to specify the signature (argument and
# return types) of functions and methods. Type annotations are a
# relatively new feature of Python, but they are supported well by
# PyCharm.
# 
# Type annotations make it possible to specify the
# _signature_ of a function very compactly, compared to describing
# argument types in a docstring. Instead of this:
# 
# ```python
# def frobnaz(n, s):
#     """frob the naz.
#     :n:  integer, frob it this many times
#     :s:  string from which we extract the naz
#     :returns: string in which the naz has been frobbed
#     """
# ```
# 
# we will write
# 
# ```python
# def frobnaz(n: int, s: str) -> str:
#     """returns copy s with its frob nazzed n times"""
# ```
# 
# An absent return type is equivalent to specifying that the function or
# method returns `None`.
# 
# Method headers follow the same rules as function signatures  `self`
# argument, as it is implied by the class.
# 
# ```python
# class Point:
#   """An (x,y) coordinate pair of integers"""
# 
#   def __init__(self, x: int, y: int):
#     self.x = x
#     self.y = y
# 
#   def move_to(self, new_x: int, new_y: int):
#     """Change the coordinates of this Point"""
#     self.x = new_x
#     self.y = new_y
# ```
# 
# As with functions, the return type annotation `-> None` may be omitted
# for methods that do not return a value. Such methods will generally be *
# mutators*, i.e., it may be assumed that they modify the value of
# the `self` object, like the
# `move_to` method above.
# 
# ### Mutation
# 
# Methods that return a value other than `None` (and which therefore have
# the `-> T`
# annotation for some type `T`) should typically *not* modify the value of
# the `self` object.
# 
# For example, if I write this function header:
# 
# ```python
# def jazziest(musicians: List[Musician]) -> Musician:
# ```
# 
# it is implicit that the input list of musicians is not modified.
# 
# On rare occasions, concise and efficient code may require a method to
# both return a  
# value *and* modify the `self` object. The
# `pop` method for lists is an example of a mutator method that returns a
# result. This is permissible but must be clearly and explicitly
# documented in the header function, and to the extent possible the
# function name should suggest that it modifies its input.
# 
# For example, if the above function returned the jazziest musician an
# also removed it from the list, the function header and docstring might
# look like this:
# 
# ```python
# def pull_jazziest(musicians: List[Musician]) -> Musician:
#     """Remove and return jazziest musician from musicians"""
# ```
# 
# ### Forward type annotations
# 
# The second case in which we cannot simply write the type of an argument
# or return value is when that type is the class we are defining.  
# The type is considered undefined until the class is complete.  
# Thus we cannot write
# 
# ```python
#     def __add__(self, other: Point) -> Point:
#       """(x,y) + (dx, dy) = (x+dx, y+dy)"""
#       return Point(self.x + other.x, self.y + other.y)
# ```
# 
# because the `Point` class does not exist yet. The workaround is to place
# quotes around the type name to indicate that it is a *forward reference*
# , i.e., a reference to a type that we promise will exist soon even
# though it does not exist quite yet.
# 
# ```python
#     def __add__(self, other: "Point") -> "Point":
#       """(x,y) + (dx, dy) = (x+dx, y+dy)"""
#       return Point(self.x + other.x, self.y + other.y)
# ```
# 
# ### Composite type annotations
# 
# Types like `int` and `str` can be used directly in type annotations.
# Types like `tuple` and `list` can also be used in type annotations, but
# typically we will prefer to be more specific, e.g., not just a `tuple`
# but more precisely
# *tuple in which the first element is a string and the second element is
# an int*. We can make this more specific annotation by importing type
# constructors from the `typing` module:
# 
# ```python
# from typing import Tuple, List, Dict
# 
# 
# def i_eat_tuples(t: Tuple[str, int]) -> Tuple[int, Tuple[int, int]]:
#     the_string, the_int = t
#     return (the_int, (the_int, the_int))
# 
# 
# def to_dict(ls: List[Tuple[str, int]]) -> Dict[str, int]:
#     result = {}
#     for key, value in ls:
#       result[key] = value
#     return result
# ```
# 
# ### Docstrings for functions and methods
# 
# A docstring should provide information that is *useful to a developer*.
# In particular, consider a developer who is building a new module that
# uses the functions or classes in your module, or who has been asked to
# add a feature to the code, fix a bug, or modify some functionality.
# Avoid noisy repetition of information that is already present in type
# hints, as well as information that is implicit. For example, the
# developer does not need to be reminded that `__init__` is the
# constructor, but may benefit from explanation of the data
# representation.
# 
# Some methods may not require docstrings at all when they follow Python
# conventions:
# 
# * An `__init__` that simply copies its arguments into instance variables
#   according to a systematic naming scheme (e.g., argument `x` might be
#   copied into `self.x` or `self._x`) may not require a docstring.
# 
# * An `__eq__` that checks for equality of some or all of its instance
#   variables, with or without a type equivalence check
#   (`type(self) == type(other)`) may not require a docstring, or the
#   docstring may briefly summarize which instance variables are
#   considered in the equivalence check.
# 
# * A single line `__str__` or `__repr__` may not require a docstring, but
#   often it will be useful to document them with an example, particularly
#   when the `__repr__` does not look exactly like a call to the
#   constructor.
# 
# 
# ## Classes: Public and quasi-private attributes
# 
# In accordance with PEP 8, object fields and methods that are meant to be
# public (that is, accessed from code outside the class or its subclasses)
# should begin with a lowercase letter. Names of fields and methods that
# are _not_ meant to be accessed directly by code outside a class should
# begin with a single underscore. (These fields and methods might be
# declared _private_ in a language with encapsulation, such as Java or
# C++, but Python does not provide encapsulation.)
# 
# In addition to the access categories described in PEP 8, we add two that
# can only be specified in docstrings:
# 
# * A docstring may describe a class as immutable (read-only), in which
#   case its public fields may be accessed but not modified by code
#   outside the class.
# 
# * In a class that is not immutable, individual fields may be described
#   as read-only, meaning that outside code may access them but must not
#   directly change them.
# 
# ## Avoid _type_ and _isinstance_
# 
# CIS 211 is a course in _object-oriented_ programming. It emphasizes
# making use of _dynamic dispatch_. Students who are not yet comfortable
# with dynamic dispatch (method calls that may have different behavior
# depending on the class of the object on which they are called) often use
# the built-in functions _isinstance_ or _type_ to control behavior. Don't
# do that. Assume that unless the instructions for a project or exam
# question specifically allow
# _isinstance_ or _type_, you should be using dynamic dispatch instead.
# Inappropriate uses of _isinstance_
# or _type_ will be marked as errors.
# 
# ### Exception: _type_ comparison in `__eq__`
# 
# There is one blanket exception to the above rule about avoiding
# `type`:  It is allowed and often a good idea to make an object
# equivalence test (the `__eq__` magic method) include a type equality
# check. For example, consider a simple `Point` class:
# 
# ```python
# class Point:
#   """2D cartesian point"""
# 
#   def __init__(self, x: float, y: float):
#     self.x = x
#     self.y = y
# 
#   def __eq__(self, other: object) -> bool:
#     return type(self) == type(other) and
#     self.x == other.x and self.y == other.y
# ```
# 
# Note that if we create a subclass `Point3D` with a z coordinate, this
# `__eq__` method will determine that `Point(5.0, 3.0, 7.0)` is not equal
# to
# `Point3D(5.0, 3.0)`; without the type check it would consider them
# equal.
# 
# ## Symbolic Constants vs Magic Values
# 
# A _magic number_ is a constant other than 0, 1, `True`, `False`, or
# `""` or `[]` that appears literally in code. For example, this snippet
# contains a magic number:
# 
# ```python
# area = radius * radius * 3.141592
# ```
# 
# For more explanation of magic numbers and why they are undesirable, see
# the "Unnamed numerical constants" section of the
# [Magic Numbers](https://en.wikipedia.org/wiki/Magic_number_(programming))
# article on
# Wikipedia. I use the concept here to refer not only to numeric
# constants, but also to strings that carry some special meaning in an
# application.
# 
# Very occasionally, if a constant is used only once, and if its meaning
# would be apparent to any developer reading the code, a magic constant
# might be acceptable. In general, though, magic numbers should be
# replaced by _symbolic constants_, e.g.,
# 
# ```python
# # Put this near the beginning of the file
# PI = 3.141592
# ...
# # Then use the symbolic name throughout
# area = radius * radius * PI
# ```
# 
# When a group of constants represent alternatives, often
# they are best represented by an _enumeration_.  Python supports
# enumerations with the `enum` package.  The main advantage of 
# enumerations over other symbolic constants is in providing a type
# that can be declared in type annotations. 
# 
# ```python
# import enum
# 
# class Color(enum.Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
# 
# light: Color  # Declare that variable light will only hold Color values
# light = Color.red
# ```
# 
# If the same constant is used in more than one code file, and especially
# if it is a value that could conceivably be changed, it should be
# factored out into a separate source file. For example, if you are
# constructing a board game with multiple source files, the size of the
# game board probably belongs in a separate source file.
# 
# 
# 
# ## Tests
# 
# We will not use doctests in CIS 211, and in most cases our docstrings
# will not include examples of use. Instead, we will use unit tests
# separate from the module code.
# 
# Unit tests may be included in the same source file as the code to be
# tested, or it may be in a separate file. If it is in a separate file,
# code to test `code.py` should be named
# `test_code.py`.
# 
# We will use the Python
# [unittest](https://docs.python.org/3.6/library/unittest.html)
# framework when practical. The _unittest_ framework may not be suitable
# for testing some features, such as interactive input and output and
# simulation results. In those cases, tests may be written using whatever
# means is appropriate, with as much test automation as feasible.
# 
# In many cases I will provide a starter test suite with a project. The
# provided test suite is _never_ exhaustive, and passing the provided test
# cases is _not_ a guarantee that a project is correct. Students are
# strongly encouraged to add their own test cases, and may sometimes be
# required to do so (that is, designing and implementing good test cases
# may be part of the project requirements).
