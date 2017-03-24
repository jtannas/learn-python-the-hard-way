#!/usr/bin/python2.7

def add(a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

weight = float(age + height) / float(iq / 2)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

''' Study Drills

Q1: If you aren't really sure what return does, try writing a few of your own functions and have them return some values. 
    You can return anything that you can put to the right of an =.
A1: I got it.

Q2: At the end of the script is a puzzle.
    I'm taking the return value of one function and using it as the argument of another function.
    I'm doing this in a chain so that I'm kind of creating a formula using the functions.
    It looks really weird, but if you run the script you can see the results.
    What you should do is try to figure out the normal formula that would recreate this same set of operations.
A2: age + height - weight * (iq / 2)

Q3: Once you have the formula worked out for the puzzle, get in there and see what happens when you modify the parts of the functions.
    Try to change it on purpose to make another value.
A3: Puzzle answer now = 0ish

Q4: Do the inverse. Write a simple formula and use the functions in the same way to calculate it.
A4: age * height - iq * iq / 10
    A4 = subtract(multiply(age, height), divide(multiply(iq, iq), 10))
'''