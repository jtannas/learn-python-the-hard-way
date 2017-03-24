#!/usr/bin/python2.7

# Define a function that takes two numbers and prints various phrases including them
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print: You have {cheese_count} crackers!
    print "You have %d cheeses!" % cheese_count
    # Print: You have {boxes_of_crackers} boxes of crackers!
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Print: Man that's enough for a party!
    print "Man that's enough for a party!"
    # Print: Get a blanket
    print "Get a blanket.\n"

# Print a phrase about how you can pass values to the function arguments
print "we can just give the function numbers directly:"
# Call the cheese_and_crackers function with values for its two arguments
cheese_and_crackers(20, 30)

# Print a phrase about how you can pass variables to the function
print "OR, we can use variable from our script:"
# Init a variable for the amount of cheese
amount_of_cheese = 10
# Init a variable for the amount of crackers
amount_of_crackers = 50

# Call the cheese_and_crackers function with the just init'd variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a phrase about how you can do math operations within the the function call 
print "We can even do math inside too:"
# Call the cheese_and_crackers function, performing some simple math within the function call
# The math is done (aka. evaluated) before the function uses it for its stuff
cheese_and_crackers(10 + 20, 5 + 6)

# Print a phrase about how you can do math operations on variables within the function call
print "And we can combine the two, variables and math:"
# Make the function call, doing some simple math witin the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)


''' Study Drills

Q1: Go back through the script and type a comment above each line explaining in English what it does.
A1: Ugly, but done

Q2: Start at the bottom and read each line backward, saying all the important characters.
A2: 

Q3: Write at least one more function of your own design, and run it 10 different ways.
A3: 
'''

def fibonacci(num):
    x = 1
    y = 1
    for i in range(0, num):
        x, y = y, x + y
    print "The %d number in the fibonacci sequence is %d" % (num, x)

fibonacci(0)
fibonacci(0 + 1)
fibonacci(1 * 2)
fibonacci(6 / 2)

mylist = range(4, 10 + 1)
for i in mylist:
    fibonacci(i)

try:
    fibonacci(int(raw_input('Please input an integer: ')))
except ValueError:
    print "That is not a valid integer"
    
from sys import argv
fibonacci(len(argv))
fibonacci(len(argv[0]))

fibonacci(100 % 17)

fibonacci(ord(argv[0][0]) % 65)
