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

# Project: Duck Machine Simulator

This week's project is the beginning of a three part "Duck Stack" 
series: 
- The Duck Machine CPU simulator (part 1, this week)
- An _assembler_ for translating assembly code into the binary
  machine code that the Duck Machine CPU executes (part 2)
- A _compiler_ that translates a simple high-level programming 
  language, Mallard, into assembly language (part 3)

Used together, these projects allow you to write a program in the 
Mallard language, translate it into machine code, and execute it on 
your Duck Machine.  

Starter code and instructions for all three stages is in a single
[github repository for the Duck Stack](
https://github.com/UO-CIS211/duck-stack).  There is a subfolder for
each stage (each level of the technology stack), as well as folders 
containing Mallard programs, test cases, and scripts to run the 
different parts of the Duck Machine project together (e.g., 
translating and then executing a Mallard program).

## Learning objectives

Primary learning objectives for this stage of the project, the Duck 
Machine CPU simulator, include

- Understanding binary representation and basic operations on binary 
  numbers, including packing and unpacking binary fields. 
- Building a basic understanding of the
[Von Neumann computer architecture](
https://en.wikipedia.org/wiki/Von_Neumann_architecture),
the fundamental structure of almost all modern computers.  Your 
  phone, your laptop, the university servers you connect to daily, 
  and likely your wristwatch are all based on the Von Neumann 
  architecture.


