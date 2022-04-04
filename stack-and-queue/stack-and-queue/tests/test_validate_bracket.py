from stack_and_queue.stack_and_queue import Stack
from stack_and_queue.validate_bracket import validate_brackets
import pytest


"""
! Test cases
    [1]- {}
    [2]- {}(){}
    [3]- ()[[Extra Characters]]	
    [4]- (){}[[]]	
    [5]- {}{Code}[Fellows](())	
    [6]- [({}]
    [7]- (](
    [8]- {(})
"""


def test_case_one():
    string = '{}'
    actual = validate_brackets(Stack, string)
    expected = True

    assert actual == expected


def test_case_two():
    string = '{}(){}'
    actual = validate_brackets(Stack, string)
    expected = True

    assert actual == expected


def test_case_three():
    string = '()[[Extra Characters]]'
    actual = validate_brackets(Stack, string)
    expected = True

    assert actual == expected


def test_case_four():
    string = '(){}[[]]'
    actual = validate_brackets(Stack, string)
    expected = True

    assert actual == expected


def test_case_five():
    string = '{}{Code}[Fellows](())'
    actual = validate_brackets(Stack, string)
    expected = True

    assert actual == expected


def test_case_six():
    string = '[({}]'
    actual = validate_brackets(Stack, string)
    expected = False

    assert actual == expected


def test_case_seven():
    string = '(]('
    actual = validate_brackets(Stack, string)
    expected = False

    assert actual == expected


def test_case_eight():
    string = '{(})'
    actual = validate_brackets(Stack, string)
    expected = False

    assert actual == expected


def test_error():
    with pytest.raises(Exception):
        string = 3
        validate_brackets(Stack, string)
