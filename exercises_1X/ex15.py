#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 15: Reading Files."""

# Import argv from the interprete sys module
from sys import argv

# Unpack the argv tuple into variables
script, filename = argv  # pylint: disable=W0632

# Commented out per the study guide
"""
# Open the file specified by the command line arguments
txt = open(filename)

# Print an introduction to the file specified
print "Here's your file %r:" % filename
# Read & Print each line of the file until EOF
print txt.read()

# close the file
txt.close()s
"""

# Ask for the filename again
print "Type the filename again:"
# Prompt for and store a filename
file_again = raw_input("> ")

# Open the newly specified file
txt_again = open(file_again)

# Read & Print the each line of the fine until EOF
print txt_again.read()

# Close the file
txt_again.close()

# End of Exercise.
"""Study Drills
This is a big jump so be sure you do this Study Drill as best you can
before moving on.

Q1: Above each line, write out in English what that line does.
A1: Ugly, but done

Q2: If you are not sure ask someone for help or search online. Many
    times searching for "python THING" will find answers to what that
    THING does in Python. Try searching for "python open."
A2: Done

Q3: I used the word "commands" here, but commands are also called
    "functions" and "methods." You will learn about functions and methods
    later in the book.
A3: Okay

Q4: Get rid of the lines 10-15 where you use raw_input and run the
    script again.
A4: Done

Q5: Use only raw_input and try the script that way. Why is one way of
    getting the filename better than another?
A5: Using argv is better because it doesn't have to halt execution
    halfway through and wait for the user. This allows other functions
    to call this script without user interference.

Q6: Start python to start the python shell, and use open from the prompt
    just like in this program. Notice how you can open files and run
    read on them from within python?
A6: Done

Q7: Have your script also call close() on the txt and txt_again
    variables. It's important to close files when you are done with them.
A7: Done
"""
