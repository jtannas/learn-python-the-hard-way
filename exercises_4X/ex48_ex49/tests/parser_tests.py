"""Parser tests

From Exercise 49 of 'Learn Python the Hard Way', 3rd Ed.
"""
### IMPORTS ###################################################################
from nose.tools import assert_equal, raises
from ex48 import parser

### pop_until_key TESTS #######################################################
# see the docstring for doctest tests


def test_pop_strings():
    """Test the function on strings"""
    lists = ['aaaa', 'bbbb', 'cccc', 'dddd']
    assert_equal(parser.pop_until_key(lists, 'c'), 'cccc')
    assert_equal(lists, ['dddd'])

    lists = ['ab12', 'bc34', 'cd56']
    assert_equal(parser.pop_until_key(lists, ['a', 'b']), 'ab12')
    assert_equal(lists, ['bc34', 'cd56'])


def test_pop_no_lists():
    assert_equal(parser.pop_until_key(None, 'a'), None)


@raises(TypeError)
def test_pop_no_keys():
    lists = ['aaaa', 'bbbb', 'cccc', 'dddd']
    assert_equal(parser.pop_until_key(lists, None), None)
    assert_equal(lists, [])


### parse TESTS ###############################################################
# see the docstring for doctest tests


### Parser TESTS ##############################################################
def test_parser():
    """Parser testing.

    The testing is pretty basic since the Parser class is just a thin
    interface for the parse function.
    """
    my_tester = parser.Parser("I run north")
    assert_equal(my_tester.plaintext, "I run north")
    assert_equal(my_tester.tokenized, [
        ('noun', 'I'),
        ('verb', 'run'),
        ('direction', 'north'),
    ])
    assert_equal(my_tester.parsed, {
        'subject': 'I',
        'verb': 'run',
        'object': 'north',
    })
    assert_equal(my_tester.subject, 'I')
    assert_equal(my_tester.verb, 'run')
    assert_equal(my_tester.object, 'north')
