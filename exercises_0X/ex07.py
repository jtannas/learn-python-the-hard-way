#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 7: More Printing."""

print "Mary had a little lamb."  # Prints the string.
print "Its fleece was white as %s." % 'snow'  # Inserts 'snow', then prints it.
print "And everywhere that Mary went."  # Prints the string.
print "." * 10  # What'd that do? A: Prints a period 10 times.

end1 = "C"  # Initiates a variable.
end2 = "h"  # Initiates a variable.
end3 = "e"  # Initiates a variable.
end4 = "e"  # Initiates a variable.
end5 = "s"  # Initiates a variable.
end6 = "e"  # Initiates a variable.
end7 = "B"  # Initiates a variable.
end8 = "u"  # Initiates a variable.
end9 = "r"  # Initiates a variable.
end10 = "g"  # Initiates a variable.
end11 = "e"  # Initiates a variable.
end12 = "r"  # Initiates a variable.

# Watch that comma at the end. try removing it to see what happens.
print end1 + end2 + end3 + end4 + end5 + end6,
# Concatenate the strings, then print without a linebreak (because the comma).
print end7 + end8 + end9 + end10 + end11 + end12
# Concantenate the strings, then print them.

# End of Exercise.
""" Study Guide

Q1: Write a comment on what each line does.
A1: Done

Q2: Read each one backward or out loud to find your errors.
A2: Done

Q3: From now on, when you make mistakes, write down on a piece of paper
    what kind of mistake you made.
A3: Variation - I'll put any mistakes that make it runtime in a
    docstring.

Q4: When moving to a new exercise, look at the mistakes you made and
    try not to repeat them.
A4: I will do my best to remember this.

Q5: Remember everyone makes mistakes.
A5: Oh yeah - programming is great because it allows us to refine our
    methods over time and to execute them consistently.
"""
