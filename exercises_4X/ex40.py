#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 40: Modules, Classes, and Objects."""


class Song(object):
    """Song example class"""

    def __init__(self, lyrics):
        """Init method, stores the input lyrics"""
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Prints the lyrics line by line"""
        for line in self.lyrics:
            print line

    def word_count(self):
        """Count the number of words in lyrics"""
        return len([word for line in self.lyrics for word in line.split()])


happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
]) #yapf: disable

bulls_on_parade = Song([
    "They rally around tha family",
    "With pockets full of shells"
]) #yapf: disable

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Write some more songs using this and make sure you understand that
    you're passing a list of strings as the lyrics.
A1: """

boy_named_sue = Song([
    "My daddy left home when I was three",
    "And he didn't leave much to ma and me",
    "Just this old guitar and an empty bottle of booze."
])

nightcall = Song([
    "I'm giving you a night call to tell you how I feel",
    "I want to drive you through the night, down the hills",
    "I'm gonna tell you something you don't want to hear"
]) #yapf: disable

"""
Q2: Put the lyrics in a separate variable, then pass that variable to
    the class to use instead.
A2: """
jingle_rock_lyrics = [
    "Jingle bell, jingle bell, jingle bell rock",
    "Jingle bells swing and jingle bells ring",
    "Snowing and blowing up bushels of fun"
]

jingle_rock = Song(jingle_rock_lyrics)
"""
Q3: See if you can hack on this and make it do more things. Don't worry
    if you have no idea how, just give it a try, see what happens.
    Break it, trash it, thrash it, you can't hurt it.
A3: Done. I broke it, then undid it.

Q4: Search online for "object-oriented programming" and try to overflow
    your brain with what you read. Don't worry if it makes absolutely
    no sense to you. Half of that stuff makes no sense to me too.
A4: Done.
"""
