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

#  Glossary of Terms

There is a lot of terminology associated with object-oriented
programming.  Often the same concept has different names (e.g., 
an _instance variable_ or _method_ may also be called an
_attribute_).   There is no need to memorize all the terms in this
glossary, but it may be helpful to you when you encounter a term
that you haven't seen before or have forgotten. 

Please open an issue to request explanations of terms that you don't 
find here. 

## A 

abstract class
: A class that cannot (or should not) be instantiated directly.
An abstract class defines a common interface contract for one or
more _concrete_ subclasses.  

abstract base class
:  Same as _abstract class_. 

attribute
:  Component of a class or object.  A _method_ may 
be called a function attribute.  An _instance variable_ may be
called a data attribute.  The `.` ("dot") operation accesses
attributes, whether they are methods or variables. 

## C

class
: A template for creating and operating on objects.
In Python 3, there is a one-to-one association between
classes and types.  For example, the constant `7` is
an `int` object, which means it has type `int` and also
that `int` is the class that specifies how `int` objects
are created and operated on.  Similarly, if you create a
class `Point`,  objects created by calling `Point` will
have type `Point`. 

## I

inherit
: If a class `C` has a method `m`, and a subclass `D` of `C`
does _not_ have a method `m`, the definition of `m` in `C` 
is _inherited_ by class `D`, as if it had been copied from `C` into `D`.

instance
: An individual object.  We may create several distinct
_instances_ from a class.  Each instance has its own set
of _instance variables_.  For example, if `p` and `r` are
instances of class `Point`, the `x` attribute
(instance variable) of `p` might be 7, while the `x` attribute
of `r` might be 19. 

instance variable
: A variable that is stored as part of an object. It may
also be called a _data attribute_.   Each object of some
class is called an _instance_ of that class, and each instance
contains its own _instance variables_.  

## L

Liskov substitution principle
: In a nutshell, the _Liskov substitution principle_
or _LSP_ (named for 
Nancy Liskov, a programming languages researcher) states that
subclasses should behave like subtypes.  If `s` is a subtype of
`t`, then we expect `s` to obey the specification of `t`, i.e., 
we should be able to use an `s` object anywhere a `t` object is 
specified.  For example, if we are looping through a list of `t` 
objects, mixing a few `s` objects into the list should not cause
a problem.  Python does not enforce _LSP_.  It is up to the
programmer to design subclasses so that they are fully compatible
with their superclasses. 

## O

override
: If a class `C` has a method `m`, and a subclass `D` of `C`
also has a method `m`, the definition of `m` in `D` _overrides_
the definition in `C`.  If `c` is an instance of `C` and
`d` is an instance of `D`, `c.m()` will execute the method `m`
defined in `C`, but `d.m()` will execute the method `m` defined in `D`.

## S 

subclass
: A subclass of some class `C` is a class defined starting
with `C` and the specifying differences, such as added _methods_
and _instance variables_ or overridden methods.  In Python 3,
a subclass is also a _subtype_. 

subtype
: A subtype is a type associated with a subclass. If a program
complies with the _Liskov substitution principle_, an instance
of a subclass should be usable wherever an instance of its
superclass is expected. 

superclass
: If 'D' is a subclass of 'C', then 'C' is the superclass of 'D'.
(Although Python permits a class to have more than one
superclass through _multiple inheritance_, in our course we will
restrict our attention to _single inheritance_, in which each class
has exactly one superclass.)





