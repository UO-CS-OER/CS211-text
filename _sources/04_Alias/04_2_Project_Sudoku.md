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

# Project: Sudoku Solver (part 1)

You will find starter code and instructions for
a [Sudoku solver](https://github.com/UO-CIS211/Duck_Sudoku) on 
github as usual.  

Most students find this project quite challenging. Give yourself 
some time, including some time in help hours or scheduled time for 
discussion and mutual help with classmates if possible. 

The Sudoku project can be completed in three stages: 
- In the first stage, you will build a representation of the Sudoku 
  board, and an algorithm for checking whether the board is complete 
  and consistent (i.e., a valid solution).
- In the second stage, you will implement two basic algorithms for 
  filling in missing tiles based on information in rows, columns, 
  and blocks.  Applying these algorithms repeatedly to _propagate_ 
  constraints is enough to solve many easy Sudoku puzzles. 
- In the third stage, you will write a recursive guess-and-check 
  procedure that can solve _any_ valid Sudoku puzzle.  The 
  guess-and-check algorithm is sufficient to solve puzzles by itself,
  but it is much faster when combined with the constraint 
  propagation techniques from the second stage. 

You can complete the first and second stages using the concepts in 
this chapter, "aliasing on purpose".  Read the next chapter, 
"recursive guess and check", before tackling the third stage. 

## Learning objectives

There is a lot going on in this project!  Key learning objectives 
include: 
- Reinforcing your grasp of aliasing, which allows us to keep 
  references to the same object in multiple collections (on purpose, 
  this time).  
- Practice in devising and coding loop algorithms on lists.  The 
  _hidden single_ and _naked single_ solving techniques are both 
  multi-pass algorithms using lists and sets. 
- Introduction to _constraint propagation_ as a general 
  problem-solving technique.  This and the recursive guess-and-check 
  algorithm in the third stage are fundamental algorithmic 
  techniques that are often used in artificial intelligence among 
  other domains.

