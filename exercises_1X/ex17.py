#!/usr/bin/python2.7
# pylint: disable = C0103, W0105
"""Exercise 17: More Files."""

from sys import argv
from os.path import exists

script, from_file, to_file = argv  # pylint: disable = W0632

print "Copying from %s to %s" % (from_file, to_file)

# we could do these on one line, how?
in_file = open(from_file)
indata = in_file.read()
# Joel's guess: indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# End of Exercise.
""" Study Drills

Q1: This script is really annoying. There's no need to ask you before
    doing the copy, and it prints too much out to the screen. Try to
    make the script more friendly to use by removing features.
Q1: """
script, from_file, to_file = argv  # pylint: disable = W0632

in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
"""
Q2: See how short you can make the script. I could make this one line
    long.
    *No way you can make this one line!*
    That ; depends ; on ; how ; you ; define ; one ; line ; of ; code.
A2: Semicolons are cheating.
    Here are two four line versions that don't commit atrocities.
"""
### Version that opens the files ######################################
# from sys import argv
script, from_file, to_file = argv  # pylint: disable = W0632
with open(from_file, 'r') as infile, open(to_file, 'w') as outfile:
    outfile.write(infile.read())

### Version that just does a copy #####################################
# from sys import argv
from shutil import copy
script, from_file, to_file = argv  # pylint: disable = W0632
copy(from_file, to_file)
"""
Q3: Notice at the end of the {What You Should See} I used something
    called cat? It's an old command that "con*cat*enates" files together,
    but mostly it's just an easy way to print a file to the screen.
    Type man cat to read about it.
A3: Heh, man cat. Done,

Q4: Find out why you had to write out_file.close() in the code.
A4: Because otherwise there's the risk of the out_file object hanging
    out in memory much longer than needed. Some interpreters will clean
    it up with a garbage collector, but you don't want to rely on it.
    The other part is that the script doesn't use 'with' the take care
    of that for us with context managers (-_-)

Q5: Go read up on Python's import statement, and start python to try it
    out. Try importing some things and see if you can get it right. It's
    alright if you do not.
A5: Done
"""
