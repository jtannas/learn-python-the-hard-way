#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 31: Making Decisions."""

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of much. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Make new parts of the game and change what decisions people can
    make. Expand the game out as much as you can before it gets
    ridiculous.
A1: I'll pass; I'm familiar with nesting if-statements and would like to
    keep moving.

Q2: Write a completely new game. Maybe you don't like this one, so make
    your own. This is your computer, do what you want.
A2: https://scratch.mit.edu/projects/128811548/
"""
