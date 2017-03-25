#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 11: Asking Questions."""

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# End of Exercise.
""" Study Guide

Q1: Find out what raw_input does
A1: If an argument is provided, it prints it as a prompt for an input.
    Then it takes the user input from the terminal and reads it into its
    return value.

Q2: Can you find other ways to user it? Try some samples you find.
A2: Done

Q3: Write another form like this to ask some questions.
A3: """
user_number = 0
while user_number <= 10:
    try:
        user_number = int(raw_input('Input an integer greater than 10: '))
    except ValueError:
        print 'That is not a valid number'

print 'Thank you for the %d!' % user_number
"""
Q4: Related to escape sequences, try to find out why the last line has
    '6\'2"' with that \' sequence. See how the single-quote needs to be
    escaped because otherwise it would end the string?
A4: Because it was printed with %r, which does the least amount of
    formatting it can get away with to print the string.
"""
