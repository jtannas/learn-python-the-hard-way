#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 33: While Loops."""


def list_numbers(limit, start=0, increment=1):
    """Create a list of numbers"""

    # Before study drill 5
    """
    i = start
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers
    """
    return range(start, limit, increment)


print "The numbers: "

for num in list_numbers(limit=6, start=0, increment=1):
    print num

### End of Exercise. ##################################################
"""Study Drills
Q1: Convert this while-loop to a function that you can call, and
    replace 6 in the test (i < 6) with a variable.
A1: Done.

Q2: Use this function to rewrite the script to try different numbers.
A2: Done.

Q3: Add another variable to the function arguments that you can pass in
    that lets you change the + 1 on line 8 so you can change how much it
    increments by.
A3: Done; it is called 'increment'.

Q4: Rewrite the script again to use this function to see what effect
    that has.
A4: Done.

Q5: Write it to use for-loops and range. Do you need the incrementor in
    the middle anymore? What happens if you do not get rid of it?
A5: It is no longer needed. If you don't get rid of it, the value would
    increment twice over the couse of a for loop.
"""
