#!/usr/bin/python2.7

# import argv from the interpreter module
from sys import argv

# unpack the argv tuple into individual variables
script, input_file = argv

# define a printall function, an alias for 'print file.read()'
def print_all(f):
    print f.read()

# define a rewind function that sets the current file read line to line 0
def rewind(f):
    f.seek(0)
    
# define a function that prints the current file line number, followed by the line contents
def print_a_line(line_count, f):
    print line_count, f.readline()

# init a variable with an opened file.
current_file = open(input_file, 'r')

# print an intro phrase about printing the whole file
print "First let's print the whole file:\n"

# print the contents of the file to the terminal
print_all(current_file)

# print a phrase explaining that the next operation is to rewind to the beginning of the file
print "Now let's rewind, kind of like a tape."

# perform the rewind using the function defined earlier in the module
rewind(current_file)

# print a phrase explainging that the next step is printing three lines
print "Let's print three lines:"

# Init a variable to tell the user the current line (not actually connected to the current line)
current_line = 1
# print the current_line variable, then print the next line in the file
print_a_line(current_line, current_file) # current_line = 1

# increment the current_line variable
current_line += 1
# print the current_line variable, then print the next line in the file
print_a_line(current_line, current_file) # current_line = 2

# increment the current_line variable
current_line += 1
# print the current_line variable, then print the next line in the file
print_a_line(current_line, current_file) # current_line = 3

''' Study Drills
Errors Made:
    For rewind, I typed in 'print fseek(0)' when the print wasn't needed.
        This resulted in 'none' being printed.
        
        
Q1: Write English comments for each line to understand what that line does.
A1: WHY SO MUCH UGLY COMMENTING??? Done.

Q2: Each time print_a_line is run, you are passing in a variable current_line.
    Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
A2: Done
    
Q3: Find each place a function is used, and check its def to make sure that you are giving it the right arguments.
A3: Done

Q4: Research online what the seek function for file does.
    Try pydoc file and see if you can figure it out from there.
    Then try pydoc file.seek to see what seek does.
A4: file.seek(line_offset,[optional whence])
    f.seek moves to a line in a file.
    The position of that line is defined by an offset from a chosen position (whence).
    The options for whence are
        0: the start of the file
        1: the current line
        2: the end of the file

Q5: Research the shorthand notation += and rewrite the script to use += instead.
A5: Done
'''