#!/usr/bin/python2.7

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

''' Study Guide

Q1: Do your checks, write down your mistakes, and try not to make the same mistakes next exercise.
A1: I tend to make small errors when typing in strings from another source.
    To counter this, I have taken to saying them out loud when reading and typing them.
    
Q2: Notice that the last line of output uses both single-quotes and double-quotes for individual pieces.
    Why do you think that is?
A2: There is a single quote in the string, so double-quotes are necessary to prevent premature termination of the string.
'''