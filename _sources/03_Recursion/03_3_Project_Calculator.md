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

# Project:  A Calculator

You will find starting files for
[the calculator project](https://github.com/UO-CIS211/calculator) on 
github as usual. 

You will build a simple interactive calculator that uses only 
integers (not floating point numbers).  You will work primarily on a
postfix (a.k.a. "reverse Polish notation", or RPN) interface that 
you can use from the command line like this: 

```text
Expression (return to quit):3 5 * x =
x = (3 * 5) => 15
Expression (return to quit):x 2 *
(x * 2) => 30
Expression (return to quit):
Bye! Thanks for the math!
```

## Learning objectives

The key learning objective for this project is becoming familiar 
with the way dynamic method dispatch can be used to organize a 
recursive algorithm for a recursive data structure. (It's not as 
scary as that might sound.)

You have written recursive functions before, typically with an `if` 
statement that distinguishes between the base case(s) and recursive 
case(s).   An expression will be represented by a recursive data 
structure, a tree in which _leaves_ are the base case and _internal 
nodes_ are the recursive case.  Instead of an _if_ statement 
determining whether to apply the base case or recursive case of an 
algorithm for expression evaluation, you will use dynamic 
dispatch.  You will implement the base 
case of the algorithm in the leaves of the data structure and the 
recursive case of the algorithm in the internal nodes, using the 
same method name.  When you call the method, either a base case or 
recursive case is selected automatically.

Additional learning objectives include: 

- "Refactoring" redundant code from concrete subclasses into a shared 
abstract base class.

- Using dynamic dispatch to tie together refactored code. 
Specifically, abstract base classes `BinOp` and `UnOp` will refer to 
methods and fields that exist only in the concrete subclasses like 
`Plus` and `Neg`.

- Recursive traversal of object structures. `__str__`, `__repr__`, and 
`eval` will make recursive calls in a style that is a little different
from recursive functions you have written before.


