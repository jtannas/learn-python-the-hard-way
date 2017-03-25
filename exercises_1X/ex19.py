#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 19: Functions and Variables."""


# Define a function that takes two numbers and prints various phrases with them
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """Takes two numbers and prints a series of phrases with them"""
    # Print: You have {cheese_count} crackers!
    print "You have %d cheeses!" % cheese_count
    # Print: You have {boxes_of_crackers} boxes of crackers!
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Print: Man that's enough for a party!
    print "Man that's enough for a party!"
    # Print: Get a blanket
    print "Get a blanket.\n"


# Print a phrase about how you can pass values to the function arguments.
print "we can just give the function numbers directly:"
# Call the cheese_and_crackers function with values for its two arguments.
cheese_and_crackers(20, 30)

# Print a phrase about how you can pass variables to the function.
print "OR, we can use variable from our script:"
# Initiate a variable for the amount of cheese.
amount_of_cheese = 10
# Initiate a variable for the amount of crackers.
amount_of_crackers = 50

# Call cheese_and_crackers with the just initiated variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print about how you can do math operations within the the function call.
print "We can even do math inside too:"
# Call cheese_and_crackers, performing simple math in the function call.
# The math is done (aka. evaluated) before the function uses it.
cheese_and_crackers(10 + 20, 5 + 6)

# Print about how you can do math operations on variables in the function call.
print "And we can combine the two, variables and math:"
# Make the function call, doing some simple math witin the arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

# End of Exercise.
""" Study Drills
Q1: Go back through the script and type a comment above each line
    explaining in English what it does.
A1: Ugly, but done

Q2: Start at the bottom and read each line backward, saying all the
    important characters.
A2: Done

Q3: Write at least one more function of your own design, and run it 10
    different ways.
A3: Done
"""


def fibonacci(n):
    """Returns the nth number (from 0) in the fibonacci sequence"""
    x, y = 0, 1
    for i in xrange(0, n):
        x, y = y, x + y
    print "Number %d in the fibonacci sequence is %d" % (n, x)


# Calling fibonacci using simple math calls.
fibonacci(0)
fibonacci(0 + 1)
fibonacci(1 * 2)
fibonacci(6 / 2)

# Calling fibonacci using iteration.
[fibonacci(x) for x in range(4, 10 + 1)]

# Calling fibonacci using user input
try:
    fibonacci(int(raw_input('Please input an integer: ')))
except ValueError:
    print "That is not a valid integer"

# Calling fibonacci in odd ways using argv
from sys import argv
fibonacci(len(argv))
fibonacci(len(argv[0]))
fibonacci(ord(argv[0][0]) % 65)

# Calling fibonacci with modulo math
fibonacci(100 % 17)
