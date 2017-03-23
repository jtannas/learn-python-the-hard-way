#!/usr/bin/python2.7

# Init cars with a value of 100
cars = 100

# Init space_in_a_car with a value of 4.0
space_in_a_car = 4.0

# Init drivers with a value of 30
drivers = 30

# Init passengers with a value of 90
passengers = 90

# Init cars_not_driven with (cars - drivers), assumes cars > drivers
cars_not_driven = cars - drivers

# Init cars with (drivers), assumes cars_driven > 0
cars_driven = drivers

# Init carpool capacity with (cars_driven * space_in_a_car)
carpool_capacity = cars_driven * space_in_a_car

# Init average_passengers_per_car with (passengers / cars_driven)
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "Thee will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

''' Study Drills

Q0:
When I wrote this program the first time I had a mistake, and Python told me about it like this:

    Traceback (most recent call last):
      File "ex4.py", line 8, in <module>
        average_passengers_per_car = car_pool_capacity / passenger
    NameError: name 'car_pool_capacity' is not defined
Explain this error in your own words. Make sure you use line numbers and explain why.

A0:
The author misspelled carpool_capacity (he spelled it: car_pool_capacity).
When python went looking for the variable he typed, it could not find it.
It then threw the error, claiming (correctly) that his variable had not been defined.

Q1:
I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?

A1:
Writing 4.0 instead of 4 makes the variable a floating point number instead of an integer.
This affects how the variable is stored in memory and how calculations with it are done.
In this example, it makes the results of 'cars_driven * space_in_a_car' a floating point number.

Q2:
Remember that 4.0 is a floating point number.
It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

A2: 
Done

Q3:
Write comments above each of the variable assignments.

A3:
It's ugly as sin, but it's done.

Q4:
Make sure you know what = is called (equals) and that it's making names for things.

A4:
Done

Q5:
Remember that _ is an underscore character.

A5:
Done

Q6:
Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations.
Popular variable names are also i, x, and j.

A7:
Done
'''
