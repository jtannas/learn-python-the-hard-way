#!/usr/bin/python2.7
"""Room class for exercise 47 (testing intro)"""


class Room(object):
    """Game room class"""

    def __init__(self, name, description):
        """Use a name and description to init a room"""
        self.name = name
        self.description = description
        self.paths = {}
        self.victory = "All your base are belong to us"

    def go(self, direction):
        """Return a path specified by a direction"""
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """Add paths to the room"""
        self.paths.update(paths)
