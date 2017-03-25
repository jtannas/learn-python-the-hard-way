#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 29: What If."""

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
In this Study Drill, try to guess what you think the if-statement is
and what it does. Try to answer these questions in your own words
before moving on to the next exercise:

Q1: What do you think the if does to the code under it?
A1: Executes the block of indented coded if the provided statement
    evaluates to true.

Q2: Why does the code under the if need to be indented four spaces?
A2: This distinguishes it from regular, non-conditional code.

Q3: What happens if it isn't indented?
A3: Then python complains about a missing indented block.

Q4: Can you put other boolean expressions from Exercise 27 in the
    if-statement? Try it.
A4: You can do that.

Q5: What happens if you change the initial values for people, cats, and dogs?
A5: Then it's possible that the logical statements will evaluate
    differently than before, and different lines will be printed. In
    other words, the code behaves different based on the inputs, but
    the code itself remains the same.
"""
