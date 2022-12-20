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

# A Course in Computational Thinking

_Introduction to Computer Science_ is a foundational course in 
computer science.  It is a course in programming, but more than that,
it is a course in computational thinking.  

What's so special about _computational_ thinking and problem solving?
Is it a branch of engineering, or math, or is it a science?
Computing certainly draws from all of those fields, and also 
contributes to them, but in some ways it is unique.

Computing and computer science do not seek to characterize the 
natural world, although many computer programs (e.g., environmental 
models, computer aided design and numerical control) incorporate 
models of the natural world.  Computing is increasingly a core tool 
used in the natural sciences, and computational thinking can be 
useful to scientists, but core concerns of the natural sciences and 
computing are distinct.  

Some areas of computing (particularly usability and user interface 
design, and software engineering) draw heavily from the social 
sciences, especially psychology but also fields as diverse as 
anthropology, linguistics, and economics.  Despite some overlap, 
though (e.g., economic game theory in the design of computer network 
protocols, visual attention in user interface design), the core 
concerns of computing are mostly distinct from the core concerns of 
the social sciences. 

Like mathematics, computing requires 
rigorous reasoning about formal, abstract systems.   
Some areas of computer science produce mathematical proofs, as you 
will be required to do if you continue with computer science through 
courses in data structures and algorithms.  
However, computer scientists are more concerned than mathematicians 
with the _things_ their formal systems represent.  

Like engineers, computer scientists and software developers
construct abstract 
representations of _things_ to 
reason  effectively about them. 
There is an important difference in the kinds of _thing_ that 
computing produces, relative to conventional engineering.
The design of a bridge or an automobile is 
complex and expensive, but the main expense of building a bridge is 
in the physical construction, and not the design.
The cost of building cars at industrial scale is likewise much larger
than the cost of designing a car.  

The _things_ designed (but not constructed) by 
software developers are _computations_. 
The computations are 
constructed by computers, following our designs. 
Computations 
are weightless and cheap.  
The designs of those computations, which we call 
_programs_ or _software_ or perhaps _software systems_, are complex 
and expensive. Any part of the construction that can be fully 
automated becomes cheap, but there always remains some part of the 
design that is necessarily human, complex, and demanding.  
Computing exposes the expense of design by removing the
limits of engineering physical things. 

All these things that computing is _not_ may shed some light on what 
computing and computer science _are_.  Computer science is concerned 
with 
_design_ of computations, and like other design disciplines it 
requires creative problem-solving. It requires forming and using 
abstract, often mathematical models, without losing track of their 
relation to concrete artifacts.  It especially requires 
careful control of complexity, decomposing problems into smaller 
sub-problems and organizing them to maintain intellectual control. 
Many disciplines incorporate these concerns to some extent, but they 
are the very core of computing. 

In tackling a core, rigorous course in computing, you should 
certainly become a better programmer.  But if skill in programming 
is the only thing you gain from this course, then we have failed.
If you as a learner and we as your teachers are successful, a 
rigorous course in computational thinking will make you a better and 
more creative problem solver.

## Learning to Program

The principles and techniques
you will learn in _Introduction to Computer Science_
are not limited to a single programming
language, let alone a particular computer or operating system.
But we have to start somewhere.  That _somewhere_
requires us to choose a programming language, and to
practice using it. 

### Why Python

In this course we will use Python, 
specifically Python version 3.10 or higher. 
Python is widely used in data science and scientific
computing, in cartography, in web development,
in machine learning, and in many other domains, but
that is not why we have chosen it. We have chosen Python 3 because 
we believe it is a good language for _learning to program_.   Python 
3 is 

- Consistent.  There are few "special cases" to remember in Python,
  which makes it easier to remember how things work and to build on 
  what you know. 
- Concise.  Python does not require a lot of boilerplate, which 
  makes it easier to read example code. 
- Well-provisioned.  Although there are many extras that you _could_ 
  add, a standard and straightforward installation of Python is 
  enough to build many interesting projects.

That is not to say that Python is a perfect language.  It is 
certainly not the only programming language you will ever want or 
need to learn.   But among the programming langauges available to us 
today, we believe it is an excellent starting point. 

## Getting a Start

The pre-requisites for _Introduction to Computer Science_ include
a basic familiarity with programming.  That familiarity may 
take many forms (not necessarily programming in Python).  Also, 
student knowledge from a course some time ago or from self study may 
be rusty or incomplete.  

If you have not programmed at all, but want to tackle this very 
demanding course, we can recommend the 
[Computer Science Circles](https://cscircles.cemc.uwaterloo.ca/)
online lessons as a good and thorough introduction.  Even if 
you have programmed in Python before, you may find the CS Circles 
materials valuable as a refresher. 

The remaining sections of this chapter provide brief instructions 
for installing Python 3 on the computer you will use for your 
projects, and then _just enough_ introduction to Python programming 
to tackle an initial project.  

* [Install Python](01-02-Install.md)
* [Python Programming Kickstart](01-03-Kickstart.md)
