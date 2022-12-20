#! /bin/bash
#
#  Execute this script from the top level of the project file to rebuild
#  the HTML version of the book from sources in Intro_to_CS.  The result
#  will appear in Intro_to_CS/_build
#
source env/bin/activate
jupyter-book build Intro_to_CS
