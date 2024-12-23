# Project:  Overlapping Appointments

[Agenda](https://github.com/UO-CIS211/Agenda) is our 
first project with user-written classes.  

## Overview 

In this project you will 

- Create a class `Appt` (short for "appointment") that represents
  a single appointment with a start time, an end time, and a
  description.  For example, you might create an `Appt` object to
  represent CS 210 lecture from 10am to 11:20am on January 7, 2025.
  - The `Appt` class will make use of the 
    `datetime` class from the Python library, which you will import.
  - Each `Appt` object will contain three _instance variables_, also 
    known as _fields_.  Two of these, 
    the start time (e.g., 10:00am on January 7, 2025) and end time 
    (e.g., 11:20am on January 7) will be represented by
    `datetime` objects. The third instance variable will be a
    description represented as a `str` object. 
  - You will write several methods for the `Appt` class.  These 
    include _magic methods_ for comparing `Appt` objects.  We will 
    interpret `<` as _before_, so that `app1 < app2` will mean
    "the end of app1 is no later than the beginning of app2". 
  - You will write an `overlaps` method.  `app1.overlaps(app2)` will 
    mean that there is a non-zero overlap in the periods represented 
    by `app1` and `app2`. 
  - You will write an `intersect` method, which creates a new `Appt` 
    object representing the overlapping portion of two appointments. 
  - You will write additional methods for creating and 
    printing `Appt` objects. 
- Create a class `Agenda` representing a collection of `Appt` 
  objects. An `Agenda` object will be a _wrapper_ for a `list` 
  object.  It will have a single instance variable, a `list` of
  `Appt` objects.  Many of its methods, like `append`, will be 
  delegated to corresponding methods of the `list` it wraps.  The 
  point of creating an `Agenda` class is to alter the behavior of 
  some methods (e.g., customizing the way a list of appointments is 
  printed) and add some new methods. 
  - You will write a `conflicts` method to detect _any_ overlap in 
    two `Agenda` objects.  The result of `ag1.conflicts(ag2)` will be 
    another  `Agenda` object, containing an `Appt` object for 
    overlap between any `Appt` object in `ag1` and some `Appt` object
    in `ag2`.   

Most of the _Agenda_ project is not complicated
or difficult, but you can 
expect some frustration and time spent because you are using 
unfamiliar language features.  Be sure to correctly use
the methods you have defined to simplify other parts of the program 
(the _DRY_ principle, _don't repeat yourself_).  For example, when 
you write the `overlaps` method of `Appt`, make use of the `<` magic 
method by noting that if `app1.overlaps(app2)`, then neither
`app1 < app2` nor `app2 < app1`.  

The only tricky bit in the project is making the `intersect` 
method efficient.  By sorting both `Agenda` objects `ag1` and `ag2`, 
you can avoid comparing _every_ `Appt` in `ag1` with _every_ `Appt` 
in `ag2`, which would take time proportional to the product of their 
lengths.  

You will turn in one file, `appt.py`. 