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

#  Installing an Interactive Development Environment (IDE)

In [part one](https://uo-cs-oer.github.io/CS210-text) we
worked with IDLE, but simple development environment that
comes packaged with a standard Python installation.  In part
two we will make use of a more sophisticated
interactive development environment (IDE) to manage more
complex projects, and in particular to make use a more
sophisticated debugger.  

In the remainder of this section, and in subsequent chapters,
we will describe how to install and use
[PyCharm](https://www.jetbrains.com/pycharm/) or
[Visual Studio Code](https://code.visualstudio.com/)
(called VS Code for short). 

## Which should I use?

Both VS Code and PyCharm are widely used both by students and by 
professional software developers.  VS Code supports a number of programming 
languages, with support for Python through plug-in modules.  PyCharm 
is part of the JetBrains suite of IDEs (along with 
CLion for C++, WebStorm for JavaScript, etc).  The JetBrains suite 
including PyCharm is a set of commercial tools with free licenses 
for students.  VS Code is an open source project that is always free. 
Both are capable systems that are 
very suitable for class projects or for more ambitious projects you 
may undertake on your own.   Both are constantly evolving and adding 
new features, such as enhanced Python type checking and interfaces 
to AI-based suggestion systems.  As of late 2024, in our view 
neither is clearly superior to the other. 

How can you choose?  

- Your instructor may standardize on one or the other.  It is 
  impractical to repeat each example in both systems, or to offer 
  expert advice in using both, so for maximum support you may wish 
  to use the IDE your instructor chooses. 
- Your classmates may already have familiarity with one or the other.  
  Especially if you have a study group that discusses and works on 
  projects together, you will be able to help each other more 
  effectively if you use the same IDE.
- If you have a visual disability, and especially if you use the JAWS 
  screen reader, we believe the accessibility of VS Code is 
  significantly better than that of PyCharm.  The community of blind 
  programmers using VS Code with JAWS and with other screen readers 
  is much larger than the community of blind programmers using 
  PyCharm, judging by messages on the
  [visually impaired programmers mailing list](
  https://www.freelists.org/list/program-l).
- Although VS Code and PyCharm are at rough parity in features, in 
  our view the Python customization in PyCharm is currently (as of 
  late 2024) a little better than VS Code with its plugin system.  
  We notice this in particular in the interactive debugging support 
  and in creating custom run configurations.  

This online textbook was created and is currently maintained in 
PyCharm.  Despite this, starting Winter 2025 the "standard" IDE for 
CS 211 at University of Oregon will be VS Code, in view of 
preferences expressed by many students and experience adapting 
projects for visually impaired students. 

## PyCharm installation

Here are instructions for installing the professional version of 
PyCharm.  If you are installing VS Code instead,
[skip to the VS Code instructions](#nstalling VS Code).

### Obtain a license

PyCharm is provided in two versions, a free "community edition" and
a non-free "professional edition".  As a college or university student
(high school students and teachers too!)  you can obtain a free license 
for the professional edition
using this [student license application form](
https://www.jetbrains.com/community/education/#students). 
You 
will need an official university email address or identification.  
The license application typically takes a few days.

You can download and install PyCharm and use it in the 30 day free trial
while waiting for your license. 

### Download PyCharm

You can download the appropriate version of PyCharm for your 
operating system (macOS, Windows, or Linux)
from [this download page](https://www.jetbrains.com/pycharm/download/).

Install PyCharm as you would other applications.  

## VS Code installation

You will find installation packages on the
[VS Code downloads page](https://code.visualstudio.com/download).
Then follow [VS Code setup instructions](
https://code.visualstudio.com/docs/setup/setup-overview).
Be sure to install the
[Microsoft Python extension](
https://code.visualstudio.com/docs/languages/python)
to VS Code. 


