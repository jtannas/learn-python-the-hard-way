#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 35: Branches and Functions.

Takes the form of a 'Choose your own adventure' text-based game.
"""


def gold_room():
    """Control logic for the gold room encounter."""
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    """Control logic for the bear room encounter."""
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    """Control logic for the chthulhu room encounter."""
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    """Player character death control logic."""
    print why, "Good job!"
    exit(0)


def start():
    """Game startup logic"""
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which on do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills.
Q1: Draw a map of the game and how you flow through it.
A1: Done.

Q2: Fix all of your mistakes, including spelling mistakes.
A2: Done.

Q3: Write comments for the functions you do not understand.
A3: Done.

Q4: Add more to the game. What can you do to both simplify and expand it?
A4: Pass - nephew is cranky for supper.

Q5: The gold_room has a weird way of getting you to type a number. What
    are all the bugs in this way of doing it? Can you make it better
    than what I've written? Look at how int() works for clues.
A5: It requires the input string to include either a 1 or a 0 to be
    recognized as a number. This excludes many valid numbers. It also
    fails to exclude text including those characters (eg. '15 gold').
    When these are converted to integers, this will cause a runtime
    error.

    A better way is:

try:
    how_much = int(raw_input("> "))
except ValueError:
    dead("Man, learn to type a number.")
"""
