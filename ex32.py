#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 32: Loops and Lists."""

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list.
for number in the_count:
    print "This is count %d" % number

# Same as above.
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can go through mixed lists too.
# Notice we have to user %r since we don't know what's in it.
for i in change:
    print "I got %r" % i

# We can also build lists, first start with an empty one.
elements = []

# Then use the range function to do 0 to 5 counts.
for i in range(0, 6):
    print "Adding %d to the list." % i
    # Append is a function that lists understand
    elements.append(i)

# Now we can print them out too.
for i in elements:
    print "Element was: %d" % i

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Take a look at how you used range. Look up the range function to
    understand it.
A1: Done, and looked up xrange as well.

Q2: Could you have avoided that for-loop entirely on line 22 and just
    assigned range(0,6) directly to elements?
A2: Yes.

Q3: Find the Python documentation on lists and read about them. What
    other operations can you do to lists besides append?
A3: https://docs.python.org/3/tutorial/datastructures.html
        list.append(value)
        list.extend(iterable)
        list.insert(index, value)
        list.remove(value)
        list.pop([index])
        list.clear()
        list.index(value, [start index], [end index])
        list.count(value)
        list.sort(key=None, reverse=False)
        list.reverse()
        list.copy()
"""
