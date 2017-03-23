#!/usr/bin/python2.7

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
    
''' Study Drills

Q1:
Remove all the my_ from the front of all the variables.

A1:
Done

Q2:
write some variables to convert the inches and lbs to centimers and kilograms

A2: '''
centimeters_per_inch = 2.54
height_centimeters = height * centimeters_per_inch

kilos_per_lb = 0.454
weight_kilos = weight * kilos_per_lb

'''
Q3:
Search online for all the python format characters

A3:
https://docs.python.org/2.4/lib/typesseq-strings.html

Q4:
Try more formatting characters. %r is a very useful one. It's like saying "print this no matter what."

A4: '''
print "This is %s. It's value is %r" % ("pi", 3.14159265)
