"""Lexicon tests

From Exercise 48 of 'Learn Python the Hard Way', 3rd Ed.
"""

from nose.tools import assert_equal, raises
from ex48 import lexicon


# see the docstring for more basic doctest tests
def test_directions():
    """lexicon directions testing"""
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east'),
    ])


def test_verbs():
    """lexicon verbs testing"""
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat'),
    ])


def test_stops():
    """lexicon stops testing"""
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of'),
    ])


def test_nouns():
    """lexicon nouns testing"""
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [
        ('noun', 'bear'),
        ('noun', 'princess'),
    ])


def test_numbers():
    """lexicon numbers testing"""
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234 -1 3.14159")
    assert_equal(result, [
        ('number', 3),
        ('number', 91234),
        ('number', -1),
        ('number', 3.14159),
    ])


def test_errors():
    """lexicon errors testing"""
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'princess'),
    ])


def test_caps():
    """lexicon capitalization testing"""
    assert_equal(lexicon.scan("GO"), [('verb', 'GO')])
    result = lexicon.scan("go KiLl eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'KiLl'),
        ('verb', 'eat'),
    ])


@raises(AttributeError)
def test_non_string():
    """lexicon non-string input exception raising test"""
    lexicon.scan(1234)
