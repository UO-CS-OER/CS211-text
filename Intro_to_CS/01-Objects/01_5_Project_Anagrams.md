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

# Project:  Multi-Word Anagrams

In the [multi-word anagram project](
https://github.com/UO-CIS211/Anagrams) we want to find possible 
anagrams of
words and phrases, including phrases of more than
one word.  For example, if we search for anagrams
of "computer science", we should find that
"eccentric mop use" and "secret income cup" are
among the possible anagrams.

In a [prior project](https://github.com/UO-CS210/jumbler)
we used a trick to find single word anagrams:  A word and
each of its single-word anagrams are identical when _normalized_ by
listing its letters in alphabetical order.  This made it
possible to compare a normalized version of a jumbled word
with the normalized version of each word in a word list. 

This normalization trick is not sufficient for finding
anagrams that are made of multiple words.  In this project
we will build a multi-word anagram finder using
a recursive algorithm and
a Python class for a _bag_ (also called a _multiset_) of
letters. 

## Learning objectives

The primary learning objectives of this project are
advancing your grasp of

- Python classes and objects. You will construct a moderately
  complex class (`LetterBag`) that records the letters that
  are available and must be used to complete an anagram. 
- Recursive search. Each time we find a word that _could_ be
  included in an anagram, we will consider two possibilities:
  We could include that word, or we could omit it and use the
  letters in a different way.  One of these possibilities will
  be explored with a recursive call.
- Aliasing.  Because our search considers multiple ways 
  to complete a multi-word anagram, we must be careful to avoid 
  accidentally changing a partial solution that is being considered 
  on a different branch.  We have considered aliasing in prior 
  projects; what is new here is aliasing of instances variables in 
  user-written classes. 

You got some practice in creating classes, methods, and 
objects in our initial [Agenda](https://github.com/UO-CIS211/Agenda)
project. The [Anagrams](https://github.com/UO-CIS211/Anagrams) 
builds on that experience with a more complex project, so that you 
have a solid understanding of classes and objects before we 
complicate things further with subclassing and inheritance in the 
next chapter and projects.