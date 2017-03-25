#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 30: Else and If."""

# Initiate a people variable.
people = 30
# Initiate a cars variable.
cars = 40
# Initiate a trucks variable.
trucks = 15

# Test if cars is greater than people.
if cars > people:
    # If so, print an appropriate phrase.
    print "We should take the cars."
# If not, test if cars is smaller than people.
elif cars < people:
    # If so, print an appropriate phrase.
    print "We should not take the cars."
# In case the other tests failed.
else:
    # Print an appropriate phrase.
    print "We can't decide."

# Test if trucks is greater than cars.
if trucks > cars:
    # If so, print an appropriate phrase.
    print "That's too many trucks."
# If not, test if trucks is smaller than cars.
elif trucks < cars:
    # If so, print an appropriate phrase.
    print "Maybe we could take the trucks."
# In case the other tests failed.
else:
    print "We still can't decide."

# Test if people is greater than trucks.
if people > trucks:
    # If so, print an appropriate phrase.
    print "Alright, let's just take the trucks."
# In case the other tests failed.
else:
    # Print an appropriate phrase
    print "Fine, let's just stay home then."

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Try to guess what elif and else are doing.
A1: 'elif' stands for 'else-if'. It follows an 'if' or 'elif' statement
    branch. When the preceeding branch gets a False and doesn't
    execute,  'elif' evaluates a logical statement to see if it should
    execute it's own branch.
    'else' follows 'elif' (or 'if' if there are no 'elif's). It is for
    a branch that executes when the preceeding branches don't.

    Example:
        x = 1
        y = 2
        if x > y:
            print "x is greater than y"
        elif x < y:
            print "x is smaller than y"
        else:
            print "x must be equal to y"

Q2: Change the numbers of cars, people, and trucks and then trace
    through each if-statement to see what will be printed.
A2: Pass.

Q3: Try some more complex boolean expressions like cars > people or
    trucks < cars.
A3: Pass.

Q4: Above each line write an English description of what the line does.
A4: Done.
"""
