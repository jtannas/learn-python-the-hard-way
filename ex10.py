#!/usr/bin/python2.7

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

''' Study Guide

Errors:
    - Missed the period in persian_cat
    
Q1: Memorize all the escape sequences by putting them on flash cars.
A1: Nope

Q2: Use triple single quotes instead of double quotes. Can you see why you might use that instead of """?
A2: Done. It's cleaner and less typing.

Q3: Combine escape sequencves and format string to create a more complex format.
A3: formatter = 'The date is %02d/%02d/%04d \t \'That\' day...'

Q4: Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. 
    Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
A4: '''

print_me = 'I didn\'t forget to \"escape\" the quotes.'
print '%r' % print_me
print '%s' % print_me
