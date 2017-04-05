# Exercise 46: A Project Skeleton.

From this point, the exercises are no longer self-contained files.
See the projects directory for the work being done.


## Required Quiz
This exercise doesn't have Study Drills but a quiz you should complete:
***
#### Q1:

Read about how to use all of the things you installed.

#### A1:

##### pip:
"Pip installs packages" - a command line tool for installing
python packages from PyPI (the Python Package Index), thes
official third-party software repository for Python.
It can be used from the command line for single packages via:
    pip install some-package-name
or it can install many packages at once via:
    pip install -r requirements.txt
where requirements.txt is a properly formatted list of packages
to install. There are additional commands for uninstalling,
generating requirements.txt, and other useful features.

##### distribute:
Is a now deprecated fork of the SetupTools project. It
was intended to replace SetupTools as the standard, but has
since been merged back into SetupTools.
It acted as a replacement for SetupTools that took over all the
functions of SetupTools, so calls to SetupTools would be
redirected to Distribute.

##### nose:
There is a concept in coding of testing your code using other
code. For example:

    add(a, b): return a + b

    test_add(): assert add(3, 4) == 7

This is important since programmers are lazy and liable to
forget to throughly test their code when making small changes.
This can allow bugs to slip into code without people noticing.
Automated code testing takes a lot of human error out of the
picture.
In Python, the default framework for testing code is unittest,
and it is included with Python. Unittest isn't the greatest
though, so people have created alternate testing frameworks.
Nose is a test runner, independent of the framework that
searches for tests to run..
Nose is run from the command line via:

    cd path/to/project
    nosetests

It searches around within the current directory for files or
directories that contain 'test' at a word boundary, then runs
what it finds.

Nose is currently not well maintained, and newer testing
frameworks are recommended (eg. Nose2, py.test, unittest2).

##### virtualenv:
A virtual environment is like simulating another
computer inside your computer. Working in a virtual environment
allows you to install stuff and fiddle with settings without
having to worry how it will affect the rest of your computer.
This is extremly useful for when you're working on multiple
projects that depend on different versions of the same
software (eg. one project uses Python 2.7, another one uses
Python 3.6).
Virtualenv is a tool to create isolated Python environments.
There are a few others, but people are pretty happy with
virtualenv or with extending virtualenv.

See here: http://stackoverflow.com/a/41573588

***
#### Q2:
Read about the setup.py file and all it has to offer. Warning: it
is not a very well-written piece of software, so it will be very
strange to use.

#### A2:
There is a standard library in Python called distutils (Distribution
utilities) that assists with packaging projects together into easily
shareable packages. Setuptools is a library that enhances the
distutils library.
To install a package, the usage is:

    python setup.py install

To uninstall, use

    pip uninstall package-name

The installation process installs all the files that are listed under
'install_requires' in the setup.py (if needed). Scripts that are listed
in the setup.py are remembered by the terminal (or more correctly, given
an alias) so that they can be run from the terminal.

IMPORTANT NOTE: This is an area where a lot of brouhaha went down,
with people making multiple different libraries that do similar
things. Check the timestamp on anything you read.

See here: http://stackoverflow.com/a/14753678

***
#### Q3:
Make a project and start putting code into the module, then get the
module working.

#### A3:
Done.
***
#### Q4:
Put a script in the bin directory that you can run. Read about how
you can make a Python script that's runnable for your system.

A4: The module in the bin folder should not end with no extension.
E.g.

    bin/ex46_script

When mentioning in setup.py, give the location from the package root.

    'scripts': ['bin/ex46_script']

Once the package is installed, they can be run from the terminal

    $ ex46_script

***
#### Q5:
Mention the bin script you created in your setup.py so that it gets
installed.

#### A5:
Done. See A4 for details.
***
#### Q6:
Use your setup.py to install your own module and make sure it works,
then use pip to uninstall it.
#### A6:
Done.
Verified by using the bin script from the terminal, and calling a
function from within the package within the bin script.