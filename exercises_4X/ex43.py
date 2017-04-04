#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 43: Basic Object-Oriented Analysis and Design."""
pass
### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Change it! Maybe you hate this game. Could be too violent, you
    aren't into sci-fi. Get the game working, then change it to what
    you like. This is your computer, you make it do what you want.
A1: Pass.

Q2: I have a bug in this code. Why is the door lock guessing 11 times?
A2: Because the code gets the new guess after checking the number of
    guesses. At guesses == 9 (the tenth guess), it then goes and asks
    for another guess.

Q3: Explain how returning the next room works.
A3: The scene_map stores a dictionary of scene objects, with a string
    acting as the dictionary key to each object. When a scene returns
    a string, that string is meant to be a key to another scene in the
    dictionary.

Q4: Add cheat codes to the game so you can get past the more difficult
    rooms. I can do this with two words on one line.
A4: Change
        elif action == "correct choice"
    to
        elif action in ["correct choice", "cheat"]

Q5: Go back to my description and analysis, then try to build a small
    combat system for the hero and the various Gothons he encounters.
A5: Pass. There's babysitting to do.

Q6: This is actually a small version of something called a "finite
    state machine." Read about them. They might not make sense but try
    anyway.
A6: Done. Interesting stuff, I should try something with it.
    https://gamedevelopment.tutsplus.com/tutorials/finite-state-machines-theory-and-implementation--gamedev-11867
"""
