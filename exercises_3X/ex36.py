#!/usr/bin/python2.7
"""Exercise 36: Designing and Debugging.

The task is to use if-statements to create my own "choose your own
adventure" game. I didn't like how the original control logic given by
exercise 35 would stack up unfinished function calls until the code
exited, so I went a different route.
It is now a single function 'engine' that calls the other ones.
Information on what to call next is passed through an argument vector.
This style prevents the stack from growing too deep.

TODO (if this weren't just an exercise):
    - game_state should be a class, but that's a future project
    - this should be split into seperate modules
"""

### IMPORTS ###########################################################
from textwrap import TextWrapper, dedent


### GAME UTILS ########################################################
def engine():
    """The engine of the game, for running the appropriate section.

    The engine design is inspired by the 'argv' style of command line
    function calls.
    The engine loops continually while it has information to operate
    on. This information is stored in the game_state variable - a dict
    of the current game information. The 'next' key/value pair is the
    name of the next function to be called. The dict is passed to each
    function being called.

    If game_state['next'] = False is passed back from the function, the
    game is terminated.
    """
    game_state = init_gamestate()
    try:
        while game_state["next"]:
            next_func = game_state["next"]
            game_state["next"] = False  # Prevent some infinite loops
            game_state = globals()[next_func](game_state)

    except (KeyError, TypeError) as e:
        print dedent("""
        ******************************************************
        Uh-oh!
        The program sent you somewhere that's not ready.
        ******************************************************
        """)


def init_gamestate():
    """Sets the starting information for the game"""
    game_state = {"next": "start"}
    return game_state


def get_response(allowed,
                 prompt="> ",
                 incorrect="Input not recognized",
                 attempts=8,
                 print_error=True):
    """Gets a response from the user, checks for quitting

    Given a list of allowed responses, continually prompt the user for
    an input that matches one of them.
    If certain sentinel values are entered (eg. QUIT) then the entire
    program exits.
    If after many tries the user has not entered a valid response,
    the function returns None.
    """
    allowed = [x.upper() for x in allowed]
    for i in xrange(attempts):
        response = raw_input(prompt).upper()

        if response in ["Q", "QUIT", "EXIT"]:
            print "Quitting game"
            exit(0)
        elif response in allowed:
            return response
        else:
            print incorrect
    else:
        if print_error:
            print dedent("""
            ******************************************************
            You appear to be stuck.
            Remember you can enter QUIT to exit the game.
            ******************************************************
            """)

        return "#Failed"


def printf(paragraph):
    """Print a formatted paragraph"""
    tw = TextWrapper()
    paragraph = dedent(paragraph)
    tw.initial_indent = "\n"
    print tw.fill(paragraph)


### GAME PATHS ########################################################
def start(game_state):
    """Starting Menu for the game."""
    printf("""
    Welcome to the Monty Python Dungeon!
    You must defeat all members of the Python troupe at their challenges.

    You may quit at any time by entering "quit".
    Are you ready to proceed? (y/n)
    """)

    allowed = ["Y", "YES", "N", "NO"]
    response = get_response(allowed)

    if response.startswith("Y"):
        print "Then here we go!!!", "\n"
        game_state["next"] = "intro"
    elif response.startswith("N"):
        game_state["next"] = "fail"
    else:
        print "Restarting section. Please read the instructions carefully."
        game_state["next"] = "start"

    return game_state


def intro(game_state):
    """Introduces the adventure."""
    printf("""
    You have journeyed far across the lands in order to find
    and defeat the cursed villains of Monty Python's Flying Circus. You
    now stand outside their castle, rested for the final confrontation.

    The castle doors stand cracked open before you.
    Do you dare enter? (y/n)
    """)

    allowed = ["Y", "YES", "N", "NO"]
    response = get_response(allowed)

    if response.startswith("Y"):
        print "The doors creak open as you push your way inside..."
        game_state["next"] = "entrance"
    elif response.startswith("N"):
        print "That's boring. I'm quitting if you're gonna stand around."
        print "You made the narrator quit."
        game_state["next"] = "fail"
    else:
        print "Restarting section. Please read the instructions carefully."
        game_state["next"] = "intro"

    return game_state


def entrance(game_state):
    """Controller for the castle entrance"""

    # Completeness check
    if game_state.get("room_1") \
            and game_state.get("room_2") \
            and game_state.get("room_3") \
            and game_state.get("room_4") \
            and game_state.get("room_5") \
            and game_state.get("room_6"):
        game_state["next"] = "victory"
    else:
        printf("""
            You enter the castle lobby. 6 numbered doors stand before you.
            Which one do you enter (1, 2, 3, 4, 5, or 6)?
            """)
        allowed = map(str, range(1, 6 + 1))
        response = get_response(allowed)
        if response in allowed:
            game_state["next"] = "room_" + response
        else:
            print "Restarting section. Please read the instructions carefully."
            game_state["next"] = "entrance"

    return game_state


def room_1(game_state):
    """The trial of Graham Chapman"""

    if game_state.get("room_1") == "complete":
        printf("""
        The holy bits of Graham Chapman litter the room_.
        There is nothing more to do here, so you return to the entranceway.
        """)
        game_state["next"] = "entrance"
    else:
        printf("""
        The 1st among the pythons - Graham Chapman - stands before you.
        He raises a holy hand grenade above his head, ready to pull the
        pin.""")
        printf("""
        "Greetings challenger!
        Answer my question correctly, and I will surrender!
        Fail, and be blown to tiny holy bits!
        Now here it is:
        What was the name of the pirate film I directed?
        You have three chances!"
        """)
        response = get_response(
            allowed=["YELLOWBEARD"],
            incorrect="Incorrect answer!",
            print_error=False,
            attempts=3)

        if response == "YELLOWBEARD":
            printf("""
            "Well done challenger! I bid thee goodbye!"
            He then pulls the pin on the grenade, and vanishes in a
            cloud of holy smoke.
            You make your way back to the entrance.
            """)
            game_state["room_1"] = "complete"
            game_state["next"] = "entrance"
        else:
            printf("""
            "You have failed, challenger! Now be gone!"
            He whips the grenade at you, it explodes, and you are no more.
            """)
            game_state["next"] = "fail"

    return game_state


def room_2(game_state):
    """The trial of John Cleese."""
    if game_state.get("room_2") == "complete":
        printf("""
        John Cleese sits quivering in the corner, helpless. There is
        nothing left to do here so you return to the entranceway.
        """)
        game_state["next"] = "entrance"
    else:
        printf("""
        As you step through the door, John Cleese rushes at you with a
        banana. What university is the law degree hanging on his wall
        from?
        """)
        allowed = ["CAMBRIDGE", "CAMBRIDGE UNIVERSITY"]
        response = get_response(
            allowed=allowed,
            incorrect="He's still coming!",
            print_error=False,
            attempts=3)

        if response in allowed:
            printf("""
            Thinking back to your courses on how to defend yourself
            against fresh fruit, you deftly disarm him of the banana
            and eat it. He cowers in fear of your self-defence mastery.
            """)
            game_state["room_2"] = "complete"
            game_state["next"] = "entrance"
        else:
            printf("""
            John Cleese lunges forward and smushes the banana in your
            face. You die of humiliation.
            """)
            game_state["next"] = "fail"

    return game_state


def room_3(game_state):
    """The trial of Terry Gilliam."""
    if game_state.get("room_3") == "complete":
        printf("""
        "I told you never to come back here!" screams cartoon god.
        He then hurls a lightning bolt through your chest.
        """)
        game_state["next"] = "fail"
    else:
        printf("""
        You enter a writing chamber, where Terry Gilliam is working
        diligently on a cartoon. As he sits there, the celing opens up
        and the cartoon face of god appears. He reaches down and hands
        you a certificate of room completion.
        """)
        printf("""
        His voice rumbles through the room. "This is what you sought,
        and now you have it. Now be gone and never return to this place!""")

        game_state["room_3"] = "complete"
        game_state["next"] = "entrance"

    return game_state


def room_4(game_state):
    """The trial of Eric Idle."""
    print "GO AWAY!"
    game_state["room_4"] = "complete"
    game_state["next"] = "entrance"
    return game_state


def room_5(game_state):
    """The trial of Terry Jones."""
    if game_state.get("room_5") == "complete":
        printf("""
        That's quite enough now...
        """)
        game_state["next"] = "entrance"
    else:
        printf("""
        Eric Idle stands before you. "Would you please tell me some
        jokes? Things are rather boring around here..."
        """)

        get_response(
            allowed=[],
            incorrect="Another please.",
            attempts=5,
            print_error=False)

        print "Thank you for the jokes, the others will surely like them."
        game_state["room_5"] = "complete"
        game_state["next"] = "entrance"

    return game_state


def room_6(game_state):
    """The trial of Michael Palin."""
    if game_state.get("room_6") == "complete":
        printf("""
        Your friendly neighbourhood programmer fell asleep. You return
        to the entrance
        """)
        game_state["next"] = "entrance"
    else:
        printf("""
        The game programmer is tired. Please complete this quiz:
        http://www.funtrivia.com/playquiz/quiz2352301aeed18.html
        """)
        print "Did you complete quiz?"
        allowed = ["Y", "YES"]
        response = get_response(
            allowed=allowed, incorrect="", print_error=False, attempts=1)

        if response in allowed:
            printf("Thanks for cooperating!")
            game_state["room_6"] = "complete"
            game_state["next"] = "entrance"
        else:
            printf("""
            Okay... Come back later then...
            """)
            game_state["next"] = "entrance"

    return game_state


def victory(game_state):
    """Declare Victory"""
    printf("""
    As you return to the entrance room, the floor crumbles away into
    a vast treasure pit of shrubbery! Hooray for all!""")
    printf("""
    You have defeated Monty Python's flying circus and saved the day
    from unconventional comedy! You should be proud of yourself. Would
    you like to play through again? (y/n)
    """)

    allowed = ["Y", "YES", "N", "NO"]
    response = get_response(allowed)
    if response.startswith("Y"):
        print "Here we go again!"
        print "---------------------"
        game_state = init_gamestate()
    elif response.startswith("N"):
        print "Goodbye and thanks for playing!"
        game_state["next"] = False
    else:
        print "Restarting section. Please read the instructions carefully."
        game_state["next"] = "victory"

    return game_state


def fail(game_state):
    """Failure section of the game"""
    print "Would you like to try again? (y/n)"

    allowed = ["Y", "YES", "N", "NO"]
    response = get_response(allowed)
    if response.startswith("Y"):
        print "'Tis but a scratch!"
        print "---------------------"
        game_state = init_gamestate()
    elif response.startswith("N"):
        print "Goodbye and thanks for playing!"
        game_state["next"] = False
    else:
        print "Restarting section. Please read the instructions carefully."
        game_state["next"] = "fail"

    return game_state


### END OF LOGIC ######################################################
if __name__ == "__main__":
    engine()
