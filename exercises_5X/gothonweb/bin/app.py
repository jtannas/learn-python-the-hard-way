#!/usr/bin/python2.7
"""Exercise 50: Your First Website

run the application like this:
    $ python bin/app.py
    http://0.0.0.0:8080/
However, if you did this:
    $ cd bin/   # WRONG! WRONG! WRONG!
    $ python app.py  # WRONG! WRONG! WRONG!
"""

import web

urls = ('/hello', 'Index')

app = web.application(urls, globals())

# Create a 'render' object that knows how to load .html files out of templates/
render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(greet="Hello", name="Nobody")
        greeting = "%s, %s" % (form.greet, form.name)
        # render the index.html file using the 'render' object
        return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()

### End of Exercise. ##################################################
# pylint: disable = W0105
"""Study Drills
Q1: Read the documentation at http://webpy.org/ which is the same as
    the lpthw.web project.
A1: It seems close enough to Flask that I'll pick it up through the
    exercises.

Q2: Experiment with everything you can find there, including their
    example code.
A2: Pass.

Q3: Read about HTML5 and CSS3 and make some other .html and .css files
    for practice.
A3: Done.

Q4: If you have a friend who knows Django and is willing to help you,
    then consider doing Exercises 50, 51, and 52 in Django instead to
    see what that's like.
A4: Pass.
"""
