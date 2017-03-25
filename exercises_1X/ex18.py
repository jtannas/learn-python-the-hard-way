#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 18: Names, Variables, Code, Functions."""


# this one is like your scripts with argv
def print_two(*args):
    """Takes a list of arguments and prints the first two"""
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    """Takes two arguments and prints them"""
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this just takes one argument
def print_one(arg1):
    """Takes a single argument and prints it"""
    print "arg1: %r" % arg1


# this one takes no arguments
def print_none():
    """Takes no arguments and prints a phrase"""
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# End of Exercise.
""" Study Drills
Create a function checklist for later exercises. Write these checks on
an index card and keep it by you while you complete the rest of these
exercises or until you feel you do not need the index card anymore:
    Did you start your function definition with def?
    Does your function name have only characters and _ (underscore) characters?
    Did you put an open parenthesis ( right after the function name?
	Did you put your arguments after the parenthesis ( separated by commas?
	Did you make each argument unique (meaning no duplicated names)?
	Did you put a close parenthesis and a colon ): after the arguments?
	Did you indent all lines of code you want in the function four spaces? No more, no less.
	Did you "end" your function by going back to writing with no indent (dedenting we call it)?

When you run ("use" or "call") a function, check these things:
	Did you call/use/run this function by typing its name?
	Did you put the ( character after the name to run it?
	Did you put the values you want into the parenthesis separated by commas?
	Did you end the function call with a ) character?

Use these two checklists on the remaining lessons until you do not need them anymore.

Finally, repeat this a few times to yourself:
    "To 'run,' 'call,' or 'use' a function all mean the same thing."
"""
