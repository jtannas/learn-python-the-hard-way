#!/usr/bin/python2.7
# pylint: disable = C0103, R0903
"""Exercise 42: Is-A, Has-A, Objects, and Classes."""


## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    """The animal class, example"""
    pass


## Dog is-an animal
class Dog(Animal):
    """The dog class, is-an animal."""

    def __init__(self, name):
        """Init procedure for the dog class"""
        ## Dog has-a name
        self.name = name


## Cat is-an animal
class Cat(Animal):
    """The cat class, is-an animal."""

    def __init__(self, name):
        """Init procedure for the cat class"""
        ## Cat has-a name
        self.name = name


## Person is-an object
class Person(object):
    """The person class, example"""

    def __init__(self, name):
        """Init procedure of the person class"""
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = []


## Employee is-a person
class Employee(Person):
    """Employee is-a person (inherits the person class)"""

    def __init__(self, name, salary):
        """Init procedure for the employee class"""

        ## Init the person aspect of the employee object
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## Fish is-an object
class Fish(object):
    """Fish class"""
    pass


## Salmon is-a Fish
class Salmon(Fish):
    """Salmon class, is-a fish"""
    pass


## Halibut is-a fish
class Halibut(Fish):
    """Halibut class, is-a fish"""
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet satan
mary.pet.append(satan)

## frank is-an employee
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet.append(rover)

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Research why Python added this strange object class, and what that
    means.
A1: Prior to Python 2.1, classes worked differently. They are what is
    now known as 'classic classes'. Python 2.1 introduced a new way of
    creating classes with several improvements. In order to prevent the
    new style of class from breaking old code, it has to be created
    using class is-an object instead of being created by default.

    In Python3, new classes are the default. This breaks old code, but
    makes life easier in the long run (once old code is updated).

    https://unspecified.wordpress.com/2010/11/18/pythons-new-classes-vs-old-classes/

Q2: Is it possible to use a class like it's an object?
A2: Yes, as long as the class inherits object at some point.

Q3: Fill out the animals, fish, and people in this exercise with
    functions that make them do things. See what happens when functions
    are in a "base class" like Animal versus in say Dog.
A3: Pass.

Q4: Find other people's code and work out all the is-a and has-a
    relationships.
A4: Done.

Q5: Make some new relationships that are lists and dictionaries so you
    can also have "has-many" relationships.
A5: Done.

Q6: Do you think there's such thing as an "is-many" relationship? Read
    about "multiple inheritance," then avoid it if you can.
A6: It exists, but it can be sketchy if not used carefully.
"""
