#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 16: Reading and Writing Files."""

from sys import argv

script, filename = argv  # pylint: disable = W0632

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

print "But then we read it just to be sure:"
filename = argv[1]
target = open(filename, 'r')
print target.read()

print "Done reading. Closing file..."
target.close()

print "Script complete"

# End of Exercise.
"""Study Drills
Q1: If you do not understand this, go back through and use the comment
    trick to get it squared away in your mind. One simple English
    comment above each line will help you understand or at least let
    you know what you need to research more.
A1: Got it.

Q2: Write a script similar to the last exercise that uses read and argv
    to read the file you just created.
A2: Done

Q3: There's too much repetition in this file. Use strings, formats, and
    escapes to print out line1, line2, and line3 with just one
    target.write() command instead of six.
A3: Done

Q4: Find out why we had to pass a 'w' as an extra parameter to open.
    Hint: open tries to be safe by making you explicitly say you want
    to write a file.
A5: 'w' = 'write'. It opens the file in a way that allows writing data
    to the file instead of limiting you to reading data.

Q5: If you open the file with 'w' mode, then do you really need the
    target.truncate()? Read the documentation for Python's open function
    and see if that's true.
A5: It is not needed to truncate the file - that happens as part of
    opening the file in write mode.
    See here: https://docs.python.org/2/library/functions.html#open
"""
