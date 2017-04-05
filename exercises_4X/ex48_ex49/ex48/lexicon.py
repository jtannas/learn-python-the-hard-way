#!/usr/bin/python2.7
"""Lexicon Module

From Exercise 48 of 'Learn Python the Hard Way', 3rd Ed.
"""

### MODULE VARS ###############################################################
LEXICON = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    'i': 'noun',
    'open': 'verb',
    'door': 'door',
    'run': 'verb',
    'ran': 'verb',
}


### FUNCTIONS #################################################################
def scan(my_string):
    """Scan for and return the tokens associated with words

    Arguments:
        - my_string: the word(s) to find the tokens for

    Returns:
        - a list of tuples (one per word). The tuples are of the format:
            - ('token', float) if the word is a number
            - ('token', 'word') if the word is found in the lexicon
            - ('error', 'word') if the word is not found in the lexicon

    Examples:
        >>> scan("south")
        [('direction', 'south')]

        >>> scan("eAsT 123 WTF")
        [('direction', 'eAsT'), ('number', 123.0), ('error', 'WTF')]

        >>> scan(1234)
        Traceback (most recent call last):
            ...
        AttributeError: 'int' object has no attribute 'split'

    """

    # Step 000: Variable validation & preparation.
    results = []

    # Step 010: Iterate through the split string, generating tuples.
    for word in my_string.split():
        try:
            result = ('number', float(word))
        except ValueError:
            result = (LEXICON.get(word.lower(), 'error'), word)
        results.append(result)

    # Step 020: Return the list of generated tuples.
    return results
