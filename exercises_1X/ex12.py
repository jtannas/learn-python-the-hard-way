#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 12: Prompting People."""

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("how much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# End of Exercise.
""" Study Drills

Q1: In Terminal where you normally run python to run your scripts,
    type pydoc raw_input. Read what it says. If you're on Windows try
    python -m pydoc raw_input instead.
A1: Done.

Q2: Get out of pydoc by typing q to quit.
A2: Done.

Q3: Look online for what the pydoc command does.
A3: Done.

Q4: Use pydoc to also read about open, file, os, and sys. It's alright
    if you do not understand those; just read through and take notes
    about interesting things.
A4: Notes taken from the pydoc:
        open: the preferred method for opening files in your code
        file: removed in python 3, there are nerd wars about why
        os: built-in module related to Operating System methods
        sys: built-in module related to the interpreter
"""
