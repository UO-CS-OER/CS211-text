---
layout: page
mathjax: true
title:  Two Pass Algorithms
---

Sometimes as you are working through one step 
in a loop, you find that you need information 
that will be available only on a subsequent step. 
Often the solution is to split your algorithm 
into two _passes_ through the data. 
Loop through once to gather the information 
you need, then loop through again to use 
that information.  

## A Simple Example

Suppose we had a set of scores for a project: 

| Name    | Score |
|---------|-------|
|Albert| 30|
|Bertal| 24|
|Cheri| 32|
|Dolores| 22|
|Ethan| 20|
|----------|-------|

The scores might be represented as a list of tuples: 

```python
scores = [
    ("Albert", 30),
    ("Bertal", 24),
    ("Cheri", 32),
    ("Dolores", 22),
    ("Ethan", 20)
]
```

Suppose we wished to _normalize_ these scores, replacing the raw score by a 
a ratio to the average (arithmetic mean) score.  (This is a very bad idea, 
but we will suppose it for the sake of the example.)  Since Cheri's score 
is 125% of the average score, her score should be represented as 1.25.  Since 
Ethan's score is 78% of the average score, his score should be represented 
as 0.75. 

|Name   |Score  |
|-------|-------|
|Albert|1.17|
|Bertal|0.94|
|Cheri|1.25|
|Dolores|0.86|
|Ethan|0.78|

We might begin to write a simple function to build the list of tuples with normalized 
scores: 

```python
def normalize_scores(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Normalized scores are fraction of average"""
    result = [ ]
    for student, score in scores:
        normalized = score / mean  ## I need the mean here! 
        result.append((student, normalized))
    return result
```

To make this work, we need the mean value.  We could try calculating 
it as we loop through the entries: 

```python
def normalize_scores(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Normalized scores are fraction of average"""
    result = [ ]
    total = 0
    count = 0
    for student, score in scores:
        count += 1
        total += score
        mean = total / count          # This is not correct!
        normalized = score / mean
        result.append((student, normalized))
    return result
```
This doesn't work ... it divides the score by the sum _so far_ 
rather than the sum of all entries. 

We could get very fancy with a list comprehension to calculate the
sum and count each time we need them: 

```python
def bad_normalize(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Looks cute, but this algorithm is quadratic in length of list!"""
    result = [ ]
    count = len(scores)
    for student, score in scores:
        total = sum([score for name, score in scores])
        mean = total / count
        normalized = score / mean
        result.append((student, normalized))
    return result
```

This looks clever, but it is actually very bad.  While the code looks like 
it only has one loop, it is actually nested loops, because the 
`sum` and the list comprehension are actually loops through the 
list of scores.  We won't notice the inefficiency for a list of 
five scores.  We would surely notice for 
a list of 1000 scores.  

The fix is very simple:  We need to calculate the total just once. 
We loop through the list of scores once to get the total
(and perhaps also the count), and then loop through again 
to produce the normalized list:  

```python
def normalize_scores(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Normalized scores are fraction of average"""
    # Pass 1:  Gather the summary information 
    total = 0
    count = 0
    for student, score in scores:
        count += 1
        total += score
    mean = total / count
    # Pass 2: Use the summary information 
    result = [ ]
    for student, score in scores:
        normalized = score / mean
        result.append((student, normalized))
    return result
```

There are still two loops in this solution, but now they are not 
_nested_ loops.  Suppose there are _n_ entries in the 
list;  nested loops will touch each entry _n<sup>2</sup>_ times, but 
one loop followed by another loop through the same items 
will touch each entry only _2n_ times. For a list of 
1000 items, the difference is 1,000,000 vs 2000 operations. 

## Summarizing in a Table

In the example above, we just needed a couple of variables 
(`total` and `count`) to hold the summary information.  Often 
we will need more.  In that case, instead of a few summary 
variables, we may need a table of summary information. 

A typical real-life example requiring a table of summary 
information is producing cross references in text formatting. 
For example, the source code for a book to be formatted 
by the LaTeX document processing system might include 
a cross-reference entry like this: 

``` 
As we will explain in more detail later (page \ref{sec:binary}), 
executable code in computer memory is indistinguishable 
from data.
```

Another part of the document source code might indicate 
the intended page number: 

```
\Section{Binary Encoding Of Everything You can Imagine}
\label{sec:binary}

Everything is binary.  Everything. That too. 
And it's all a big undifferentiated soup of numbers
until we decide how to interpret it. 
```

The text formatting system has to essentially format the whole text twice. 
On the first pass it may discover that the label `sec:binary` appears on 
page 42.  This might be before or after the cross reference;  either way 
it saves the pair `("sec:binary", 42)` in a table, and uses that table 
on the second pass when it can substitute the page number for the 
reference. 

As a less realistic but simpler example, suppose we have a list of fruits 
like this: 

```python
fruit_bowl = ["banana", "orange", "banana", "kiwi", "banana", "orange"]
```

We want "m of n" style formatting for each item in the bowl: 

``` 
banana 1 of 3
orange 1 of 2
banana 2 of 3
kiwi 1 of 1
banana 3 of 3
orange 2 of 2
```

We will write a function `itemize_fruits` to produce the 
printed list of fruits in a bowl.  

```python
def itemize_fruits(bowl: List[str]):
    """Print the fruits as
    banana 1 of 3
    orange 1 of 2
    etc
    """
```

Keeping a count is not difficult, but we need _two_ counts for each fruit: 
the total count, and the count of items encountered _so far_.  
In the first pass through the list of fruits, we will produce the 
table of total counts: 

```python
    # Pass 1
    full_counts = { }  # We'll keep summary information here
    for fruit in bowl:
        # Ensure there is an entry for the fruit
        if fruit not in full_counts:
            full_counts[fruit] = 0
        full_counts[fruit] += 1
``` 

In the second pass, we will recompute counts and store them in a 
separate table. 

```python
    # Pass 2
    cur_counts = { }
    for fruit in bowl:
        # Ensure this is an entry for the fruit
        if fruit not in cur_counts:
            cur_counts[fruit] = 0
        cur_counts[fruit] += 1
```

We could make a third pass through the list to do the actual printing, 
but it is not necessary.  We can print as soon as we have computed the 
the second count, in the same loop: 

```python
def itemize_fruits(bowl: List[str]):
    """Print the fruits as
    banana 1 of 3
    orange 1 of 2
    etc
    """
    # Pass 1
    full_counts = { }  # We'll keep summary information here
    for fruit in bowl:
        # Ensure there is an entry for the fruit
        if fruit not in full_counts:
            full_counts[fruit] = 0
        full_counts[fruit] += 1
    # Pass 2
    cur_counts = { }
    for fruit in bowl:
        # Ensure this is an entry for the fruit
        if fruit not in cur_counts:
            cur_counts[fruit] = 0
        cur_counts[fruit] += 1
        # Now we have both pieces of information
        print(f"{fruit} {cur_counts[fruit]} of {full_counts[fruit]}")
```

## Application to the Assembler Project 

In week 8 of CIS 211, you will build the 
address resolution logic of an _assembler_, a program that translates Duck Machine assembly 
code to machine code.   What you will create actually is the first phase of the assembler, which 
resolves labels to pc-relative addresses.  Given an input program like this: 

``` 
# Determine the maximum of two integers.
# This program triggers memory-mapped IO to
# read integers from the keyboard and to
# write integers to the display.
   LOAD r1,r0,r0[510]     # Trigger read from console
   LOAD r2,r0,r0[510]     # Trigger read from console
   SUB  r0,r1,r2[0]
   JUMP/P r1bigger
   STORE r2,r0,r0[511]    # Trigger write to console
   HALT r0,r0,r0
r1bigger:
   STORE r1,r0,r0[511]    # Trigger write to console
   HALT r0,r0,r0
```

Your program will translate the label `r1bigger` into a 
PC-relative address, resulting in a modified ("resolved")
version of the program, like this: 

```
  
# Determine the maximum of two integers.
# This program triggers memory-mapped IO to
# read integers from the keyboard and to
# write integers to the display.
   LOAD r1,r0,r0[510]     # Trigger read from console
   LOAD r2,r0,r0[510]     # Trigger read from console
   SUB  r0,r1,r2[0]
   ADD/P  r15,r0,r15[3] #Jump to r1bigger
   STORE r2,r0,r0[511]    # Trigger write to console
   HALT r0,r0,r0
r1bigger:
   STORE r1,r0,r0[511]    # Trigger write to console
   HALT r0,r0,r0
```

Note that the `JUMP/P` pseudo-instruction has been translated 
to the real Duck Machine instruction `ADD/P` (add if positive), 
and that the instruction adds 3 to the program counter 
in register 15.  The relative address 3 is the _difference_ 
between address 6 at which the label `r1bigger` appears 
address 3 at which the jump appears. 

Just as we counted fruits twice above to itemize them, 
your address resolver will need to count instructions 
twice to determine the addresses.  In the first pass, 
you will create a table associating labels like `r1bigger`
with addresses by counting the number of machine instructions 
to be produced.  In the second pass, you will count 
machine instructions again, and also produce the 
modified program code. 

## Summary 

We often use multi-pass (two-pass or more) algorithms when a step in a loop 
requires information that will not be available until a future step.  We make 
(at least) one "pass" (loop) through the whole data to gather the needed 
information, and then a second "pass" to use it.  Sometimes we only 
need a summary variable or two, but often we need a table to hold whatever
information we need to summarize.   

## Example Code 

[Sample source code](../sample_code/08_twopass.py) is available for this chapter. 