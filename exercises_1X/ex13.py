#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Example 13: Parameters, Unpacking, Variables."""

from sys import argv

script, first, second, third, fourth = argv  # pylint: disable=W0632

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

# End of Eexercise.
""" Study Drills
Q1: Try giving fewer than three arguments to your script. See that
    error you get? See if you can explain it.
A1: There aren't enough members within the tuple to unpack, so the
    unpacking fails.

Q2: Write a script that has fewer arguments and one that has more. Make
    sure you give the unpacked variables good names.
A2: Done

Q3: Combine raw_input with argv to make a script that gets more input
    from a user. Don't over think it. Just use argv to get something,
    and raw_input to get something else from the user.
A4: """
user_input = raw_input("Please write in a thing:")
print "I have combined your thing of %r with the 2nd argument of %r!" % (
    user_input, second)
"""
Q4: Remember that modules give you features. Modules. Modules. Remember
    this because we'll need it later.
A4: Done.
"""
