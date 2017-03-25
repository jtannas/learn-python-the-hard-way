#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 6: Strings and Text."""

# Inserts the value 10 into the string.
x = "There are %d types of people." % 10

# Initiate a string.
binary = "binary"

# Initiate another string.
do_not = "don't"

# Inserts those two strings into a phrase.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print phrase 1.
print x

# Print phrase 2.
print y

# Repeat phrase 1 within another phrase.
print "I said: %r." % y

# Repeat phrase 2 within another phrase.
print "I also said: '%s'." % y

# Initiate a boolean varible.
hilarious = False

# Create a phrase asking if the joke was funny.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the inquiry phrase, inserting the boolean as a response.
print joke_evaluation % hilarious

# Initiate the left side of a sentence.
w = "This is the left side of..."

# Initiate the right side of a sentence.
e = "a string with a right side."

# Print the concatenation of the two sides.
print w + e

# End of Exercise.
"""Study Drills
Q1: Go through this program and write a comment above each line
    explaining it.
A1: Ugly, but done

Q2: Find all the places where a string is put inside a string. There
    are four places.
A2: Line 13 (twice), line 22, and line 25

Q3: Are you sure there are only four places? How do you know? Maybe I
    like lying.
A3: Yes, the other insertions are for booleans and integers, not strings.

Q4: Explain why adding the two strings w and e with + makes a longer
    string.
A4: + is the concatenation operator in python
"""
