#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 24: More Practice."""

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehed passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    """Return the (jellybeans, jars, crates) relative to the input number"""
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
my_beans, my_jars, my_crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (my_beans, my_jars,
                                                       my_crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(
    start_point)

# End of Exercise.
# pylint: disable = W0105
"""Study Drills
Q1: Make sure to do your checks: read it backward, read it out loud,
    and put comments above confusing parts.
A1: Done.

Q2: Break the file on purpose, then run it to see what kinds of errors
    you get. Make sure you can fix it.
A2: Done.
"""
