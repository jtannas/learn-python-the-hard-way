#!/usr/bin/python2.7
# pylint: disable = C0103
"""Exercise 39: Dictionaries, Oh Lovely Dictionaries."""

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviatred %s and has city %s" % (state, abbrev,
                                                           cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Do this same kind of mapping with cities and states/regions in your
    country or some other country.
Q1: Pass. I had lots of practice with dicts in exercise 36.

Q1: Find the Python documentation for dictionaries and try to do even
    more things to them.
Q1: Done.

Q1: Find out what you can't do with dictionaries. A big one is that
    they do not have order, so try playing with that.
Q1: Done. The ordering issue is due to how the keys are hashed. There
    is a sorted function to allow the dict keys to be sorted.
"""
