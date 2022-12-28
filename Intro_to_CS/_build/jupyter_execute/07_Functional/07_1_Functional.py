#!/usr/bin/env python
# coding: utf-8

# # Sometimes Functions are Values
# 
# Our project for week 7 largely builds on 
# concepts introduced earlier in the term,
# especially bitfield packing and unpacking but 
# also objects with other objects as fields 
# (e.g., the ALU and registers are part of the CPU, 
# and the 
# Memory is attached ("wired") to the CPU in the 
# main program), the Model-View-Controller pattern 
# attaching a graphical display to the CPU and memory 
# state, some careful sequential logic to 
# update the program counter register at the right 
# point in the execution cycle. 
# 
# One small part that may seem unfamiliar is the 
# way the ALU executes operations by looking them 
# up in a table.  We have actually seen similar 
# techniques a couple times before: 
# 
# * In the Agenda project, we passed a function to the 
#   built-in `sort` method to order appointments by 
#   start time: 
#   `self.elements.sort(key=lambda appt: appt.start)`
#   
# * In the Calculator project, we used a table of classes to avoid 
#   repetitive code while parsing the postfix expressions: 
#   `stack.append(BINOPS[tok.kind](left, right))`
#   We called the classes in the 
#   `BINOPS` and `UNOPS` tables to create 
#   objects of the classes corresponding to each symbol like 
#   `+` and `*`.  
#   
# In our simulation of the arithmetic logic unit (ALU) of the 
# Duck Machine, we will use a table in which the keys are 
# numeric operation codes and the values are functions indicated 
# by those codes.  This is very analogous to the circuitry 
# called a "multiplexer" that selects connections based on the 
# values (1 or 0, positive voltage or no voltage) on some of its 
# input wires. 
# 
# ## When should we use functions as values? 
# 
# Some programming languages allow us to treat functions as 
# values.  We can store functions in variables, pass functions to other 
# functions, return functions from functions, etc.  When we can 
# do this, we say that functions are _first class values_ in 
# the programming language.  Python is such a language. 
# 
# In some other programming languages you will learn, functions may 
# not be first class values.  Java, for example, has methods but 
# not functions, and methods are not first class values (although 
# recently a limited kind of first class function value, 
# called a *lambda expression*, was added to Java).  
# In C you will encounter 
# _function pointers_, which are first class values, although they 
# are a little trickier to define and 
# use than function objects in Python.  Each language you learn may be 
# a little different in terms of whether and how you can treat 
# functions as values. 
# 
# We use functions as values for some of the same reasons we use 
# classes and subclasses in object oriented languages:  To simplify 
# and generalize code, avoiding redundancy by factoring out 
# the parts that are repetitive. Classes and subclasses may be 
# more useful in some situations, and functions as values may be 
# more useful in others: 
# 
# * Classes and subclasses are especially useful when there is a 
#   natural subtype hierarchy to organize variation, such as 
#   organizing our calculator expression classes as binary and 
#   unary operations.   The object-oriented style is also useful 
#   when we maintain complex state, such as the fields of 
#   appointment objects in our agenda project. 
# 
# * Functions as values are sometimes more useful than classes 
#   when functions are natural building blocks, especially when 
#   we don't have as much need to maintain complex state. 
#   Functions also make good building blocks even if state is complex
#   but more uniform than the functions we want to apply. 
#   
# Sometimes either approach would be about equally applicable.  
# For example, in our calculator project, instead of creating 
# several subclasses of the `BinOp` class, we could have created 
# a single class with an instance variable holding the function 
# to be applied.  The code would have been a little shorter, 
# but whether it would have been simpler is arguable. 
# 
# ## Functional Programming in Python 
# 
# Python supports both an object-oriented style of programming 
# and a functional style of programming.  The object-oriented 
# style is more common in large projects, but sometimes 
# the functional style is just the tool we need to 
# greatly simplify some code.  Two particularly useful 
# tricks of the trade are storing functions in tables 
# (dicts) and passing functions to functions or methods.
# 
# ### Lambda is just shorthand
# 
# Often when you encounter functions as values, they are 
# written as lambda expressions, e.g., `lambda x: x + 1`. 
# There is nothing complex or mysterious about lambda.  It 
# is just shorthand for the familiar function function 
# definition, e.g., 
# ```python
# def f(x): 
#     return x + 1
# ```
# 
# The lambda expression doesn't have a name, but it is easy 
# enough to give it one: 
# 
# ```python
# f = lambda x: x + 1
# ```
# 
# The two definitions of `f` above, with a conventional function definition
# and with a lambda expression assigned to variable `f`, do 
# precisely the same thing.  We simply use the lambda expression 
# to avoid writing out the longer function definition, when 
# it fits on one line, and especially 
# when it doesn't need a name.  
# 
# ### Beyond sum:  Reduce 
# 
# You may know that you can add up the elements of a list with the
# `sum` function: 
# 
# ```python
# >>> sum([1, 2, 3, 4, 5])
# 15
# ```
# 
# What if we wanted to instead multiply all the elements, 
# or count them?   We can write a single function for all 
# of these, passing in the function by which the elements 
# are all combined to obtain a single summary value. 
# 
# ```python
# def reduce(l: List[int], initial: int, f: Callable[[int], int]) -> int:
#     """ Reduce l by f, i.e., f(el, f(el, f(el, ...))) for el in l"""
#     reduction = initial
#     for el in l:
#         reduction = f(reduction, el)
#     return reduction
# ```
# 
# The type hints are unwieldy (and would have been even more 
# unwieldy if I had written a version that works for all kinds 
# of lists, not just lists of `int`), but the code is simple: 
# It just keeps applying a function over and over to distill the 
# list to a single value.   To get a sum, I pass in a function 
# (which I can write compactly using`lambda`) to add elements: 
# 
# ```python
# li = [1, 2, 3, 4, 5]
# 
# # Reduce with + is same as sum
# assert reduce(li, 0, lambda a,b: a+b) == 15
# ```
# 
# If instead I want the product of all the elements, 
# I pass in a function that multiplies: 
# 
# ```python
# # Reduce with * is product of all elements
# assert reduce(li, 1, lambda a,b: a*b) == 120
# ```
# 
# If I want to just count the elements, I can ignore the 
# values and just add one at each step: 
# 
# ```python
# # Trickier!  We can also get a 'count' function
# assert reduce(li, 0, lambda a,b: a+1) == 5
# ```
# 
# Of course I am not limited to short nameless functions 
# written with lambda.  I can find a maximum or minimum 
# if I a careful about what to use as an initial value: 
# 
# ```python
# # Max, min, or some other selection
# def larger(x, y):
#     """For demo purposes only; built-in max is preferable"""
#     if x > y: return x
#     return y
# 
# assert reduce(li, li[0], larger) == 5
# ```
# 
# ### Walking a tree with a function value
# 
# The `reduce` function described above was intriguing, but 
# not really very useful since Python already gives us many 
# reductions on lists including `sum`, `max`, etc.  However, 
# we can use the same basic technique with other data structures, 
# where the built-in Python functions are not applicable.  
# Let's consider a simple tree of integers with a `reduce`
# method: 
# 
# ```python
# class Tree:
#     """The abstract base class"""
# 
#     def reduce(self, f: Callable[[int, int], int],
#                leaf_val: Optional[int] = None):
#         """f is a function for combining values of subtrees.
#         Leaves will return their own value unless leaf_val
#         is specified.
#         """
#         raise NotImplementedError("Each subclass must implement reduce")
# 
# class Leaf(Tree):
#     def __init__(self, val: int):
#         self.val = val
# 
#     def reduce(self, f: Callable[[int, int], int],
#                leaf_val: Optional[int] = None):
#         if leaf_val is None:
#             return self.val
#         else:
#             return leaf_val
# 
# class Inner(Tree):
#     def __init__(self, left: Tree, right: Tree):
#         self.left = left
#         self.right = right
# 
#     def reduce(self, f: Callable[[int, int], int],
#                leaf_val: Optional[int] = None):
#         return f(self.left.reduce(f, leaf_val),
#                  self.right.reduce(f, leaf_val))
# ```
# 
# We can use the `reduce` method with a function argument 
# to implement different ways of summarizing values of the 
# leaves, just as we did for a list: 
# 
# ```python
# t = Inner(Inner(Leaf(1), Leaf(2)),
#           Inner(Leaf(3), Inner(Leaf(4), Leaf(5))))
# 
# # Sum leaves of tree
# assert t.reduce(lambda v,w: v+w) == 15
# # Product of leaves of tree
# assert t.reduce(lambda v,w: v*w) == 120
# # Max/Min leaf of tree using built-in max and min
# assert t.reduce(max) == 5
# assert t.reduce(min) == 1
# # Count leaves
# assert t.reduce(lambda x,y: x+y, leaf_val=1) == 5
# ```
# 
# ### Use as needed; Don't get carried away
# 
# Function values are powerful, and sometimes they are just 
# the right tool for the job.  Other times, you can accomplish 
# the same thing with simpler approaches.  Many programmers 
# find it difficult to read code that uses function values 
# extensively.  
# 
# Functions or methods that take functions as arguments can be 
# most useful when one such function can be used in place of 
# several.  For example, if I only needed a method to sum 
# the leaves of a tree, I would write a (recursive) `sum` method, 
# and not a general `reduce` method.  But if I need `sum` and 
# `product` and `max` and `min`, then a single `reduce` method 
# becomes an attractive option.  
# 
# We have seen this in our prior projects that used function 
# arguments and tables of functions or classes.  The table of 
# classes in our calculator project replaced a chain of
# redundant `elif` ... 
# `elif` ... `elif` clauses in our parser, so it was worthwhile.
# The table of operation functions in the ALU class for the 
# Duck Machine simulator likewise allows us to avoid a chain 
# of largely repetitive code.  
# The `key=` function argument to `sort` saves us from more 
# complex ways of controlling the sort function.  Using functions 
# as values (in tables, and as arguments to methods or functions)
# is worthwhile in these contexts.  
# 
# ### There's more 
# 
# There is much more you can do with functions as values 
# in Python.  For example, frameworks for web applications, like 
# Django and Flask, create a table of functions for handling 
# different URLs.  Both Django and Flask use Python _decorators_, 
# which are functions that operate on other Python functions. 
# Don't worry if that sounds confusing ... it's not something we're 
# going to do in CIS 211.  But they are there for you sometime 
# in the future when you need them. 
# 
# You can program for years in Python only occasionally encountering
# functions as values, and maybe managing to use them without 
# really understanding them.  In some other languages, functions as 
# values play a much more central role.  If you write web application 
# code that executes in the browser, you are likely to encounter 
# JavaScript code that uses functions as values.  You may also 
# encounter some programming languages, like ML or Haskell, that 
# are called "functional languages" because functions that 
# combine other functions are as central to them as classes and 
# objects are to Python. 
# 
# ## Summary
# 
# Sometimes using a function as a value, in a table or passed 
# as an argument to another function, can greatly simplify your
# code and remove redundancy.  Python is primarily an object-oriented 
# language, not a functional language, and most of the time 
# classes and objects give us the tools we need to solve problems. 
# But sometimes a little bit of functional programming is a 
# powerful addition. 
# 
# ## Source Code 
# 
# [Sample code for this chapter](../sample_code/functional.py)
