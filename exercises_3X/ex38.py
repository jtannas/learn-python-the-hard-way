#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 38: Doing Things to Lists."""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')  #aka split(ten_things, ' ')
more_stuff = [
    "Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"
]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # aka pop(more_stuff), call pop on more stuff
    print "Adding: ", next_one
    stuff.append(
        next_one)  # aka append(stuff, next_one), append next_one to stuff
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # whoa! fancys
print stuff.pop()  # aka pop(stuff)
print ' '.join(
    stuff)  # aka join(' ', stuff), join the pieces of stuff using ' '
print '#'.join(stuff[
    3:5])  # aka join('#', stuff[3:5]), join the pieces of stuff[3:5] using '#'

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills.
Q1: Take each function that is called, and go through the steps for
    function calls to translate them to what Python does. For example,
    more_stuff.pop() is pop(more_stuff).
A1: Done.

Q2: Translate these two ways to view the function calls in English. For
    example, more_stuff.pop() reads as, "Call pop on more_stuff."
    Meanwhile, pop(more_stuff) means, "Call pop with argument
    more_stuff." Understand how they are really the same thing.
A2: Done.

Q3: Go read about "object-oriented programming" online. Confused? I was
    too. Do not worry. You will learn enough to be dangerous, and you
    can slowly learn more later.
A3: Done.

Q4: Read up on what a "class" is in Python. Do not read about how other
    languages use the word "class." That will only mess you up.
A4: Done.

Q5: Do not worry If you do not have any idea what I'm talking about.
    Programmers like to feel smart so they invented object-oriented
    programming, named it OOP, and then used it way too much. If you
    think that's hard, you should try to use "functional programming."
A5: Done.

Q6: Find 10 examples of things in the real world that would fit in a
    list. Try writing some scripts to work with them.
A6: People names, countries, book titles, pets, fruit, veggies, songs,
    devices, colours, and movies.
"""
