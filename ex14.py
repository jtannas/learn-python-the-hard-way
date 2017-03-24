#!/usr/bin/python2.7

from sys import argv

script, user_name, user_computer = argv
prompt = 'DON\'T LIE TO THE ROBOT, HUMAN: '

print "Hi %s, I'm %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
if computer != user_computer:
    print "YOU LIED TO THE ROBOT, FILTHY HUMAN!"

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


''' Study Drills

Q1: Find out what Zork and Adventure were. Try to find a copy and play it.
A1: They're basically compterized D&D. Zork is text based, adventure is GUI.
    Zork: http://textadventures.co.uk/games/view/5zyoqrsugeopel3ffhz_vq/zork
    Adventure: http://my.ign.com/atari/adventure

Q2: Change the prompt variable to something else entirely.
A2: Changed from '> ' to "DON'T LIE TO THE ROBOT, HUMAN:"

Q3: Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
A3: Done

Q4: Make sure you understand how I combined a """ style multiline string with the % format activator as the last print.
A4: Done, it's really just a different way of demarking the limits of a string.
'''