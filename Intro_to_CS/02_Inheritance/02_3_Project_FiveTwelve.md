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

# Project: A Sliding Tile Game

[FiveTwelve](https://github.com/UO-CIS211/FiveTwelve)
is a sliding tile game based on 2048, with a few changes.
2048 was itself based on an earlier game called 1024, which was
inspired by the more challenging sliding tile game Threes.

## Learning objectives

- Using subclasses and inheritance to _factor_ related behavior into 
  shared superclasses.  This is a key way object-oriented 
  programming facilitates the _DRY_ (don't repeat yourself) principle.
- Using _notifiers_ in the Model-View-Controller (_MVC_) 
  _design pattern_ to _factor_ game logic from display and 
  interaction. Although related to the _DRY_ principle, this 
  factoring of _model_ component from _view_ component is more 
  concerned with maintainability, portability, and extensibility of 
  complex applications, by allowing modification or substitution of
  view 
  components (display and interaction) without modifying the model 
  component (game logic and internal representations). 

Quite a bit of code is provided in the
[HOWTO document](
https://github.com/UO-CIS211/FiveTwelve/blob/master/doc/HOWTO.md),
but there is still a lot to understand and build.  Even if you have 
gotten away with building some prior projects in a single 
programming session, you will almost certainly need to spread this 
project over multiple sessions and multiple days with breaks to 
clear your brain when it gets clogged with details.  Build a little, 
test a little, debug a lot, and ask for help when you get stuck.  